#!/usr/bin/python

try:
    from urllib2 import urlopen
    from HTMLParser import HTMLParser
    import json   
except ImportError:
    print ImportError

import os
import json
from Contest import Contest
from Problem import Problem
from TestCase import TestCase


# this class was based on class CodeforcesProblemParser from
# https://github.com/johnathan79717/codeforces-parser/blob/master/parse.py
class TestCasesHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.tests = []
        self.curTestCase = None
        self.curData = None
        self.dataType = "input"
        self.is_copying = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            if attrs == [('class', 'input')]:
                self.curData = ""
                self.dataType = 'input'
                self.curTestCase = TestCase("", "")
            elif attrs == [('class', 'output')]:
                self.curData = ""
                self.dataType = 'output'
        elif tag == 'pre':
            if self.curTestCase is not None:
                self.is_copying = True

    def handle_endtag(self, tag):
        if tag == 'br':
            if self.is_copying:
                self.curData = self.curData + '\n'.encode('utf-8')
                self.end_line = True
        if tag == 'pre':
            if self.is_copying:
                if not self.end_line:
                    self.curData = self.curData + '\n'.encode('utf-8')
                if self.dataType == 'input':
                    self.curTestCase.input_text = self.curData
                if self.dataType == 'output':
                    self.curTestCase.output_text = self.curData
                    self.tests.append(self.curTestCase)
                    self.curTestCase = None
                self.is_copying = False

    def handle_entityref(self, name):
        if self.is_copying:
            self.curData = self.curData + \
                self.unescape(('&%s;' % name)).encode('utf-8')

    def handle_data(self, data):
        if self.is_copying:
            self.curData = self.curData + data.encode('utf-8')
            self.end_line = False


class CodeForces:

    def __init__(self, contest_db_path='contests', problem_db_path='problems'):
        self.up_to_date = False
        self.contests_path = contest_db_path
        self.problems_path = problem_db_path
        self.load_all_contests()
        self.load_all_problems()

    def load_all_contests(self, update=False):
        source_contest = "http://codeforces.com/api/contest.list"
        if update and os.path.isfile(self.contests_path):
            os.remove(self.contests_path)
        try:
            self.contests = open(self.contests_path).read()
        except:
            try:
                print "downloading contests..."
                self.contests = \
                    urlopen(source_contest).read()
                f = open(self.contests_path, 'w')
                f.write(self.contests)
                f.close()
            except:
                raise
        self.parsed_contests = json.loads(self.contests)
        if self.parsed_contests['status'] != 'OK':
                print "Error: bad contest data!"
                exit(1)
        print str(len(self.parsed_contests['result'])) + " contests loaded"

    def load_all_problems(self, update=False):
        source_problems = "http://codeforces.com/api/problemset.problems"
        if update and os.path.isfile(self.problems_path):
            os.remove(self.problems_path)
        try:
            self.problems = open(self.problems_path).read()
        except:
            try:
                print "downloading problems..."
                self.problems = \
                    urlopen(
                        source_problems).read()
                f = open(self.problems_path, 'w')
                f.write(self.problems)
                f.close()
            except:
                raise
        self.parsed_problems = json.loads(self.problems)
        if self.parsed_problems['status'] != 'OK':
            print "Error: bad problem data!"
            exit(1)
        print str(len(self.parsed_problems['result']['problems'])) \
            + " problems loaded"

    def update(self):
        if self.up_to_date:
            return
        self.load_all_contests(True)
        self.load_all_problems(True)
        self.up_to_date = True

    def contest_exists(self, contest_id, full=False):
        if full:
            fp = list(filter(lambda x: x['contestId'] == contest_id,
                             self.parsed_problems['result']['problems']))
        else:
            fp = []
        fc = list(filter(lambda x: x['id'] == contest_id,
                         self.parsed_contests['result']))
        if ((not full and not len(fc) > 0) or
            (full and (not len(fc) > 0 or not len(fp) > 0))) \
                and not self.up_to_date:
            self.update()
            return self.contest_exists(contest_id, full)
        if full:
            return len(fc) > 0 and len(fp) > 0
        return len(fc) > 0

    def get_problem(self, contest_id, pid):
        source_problem = "http://codeforces.com/contest/"
        r = list(
            filter(lambda x: x['contestId'] == contest_id and x['index'] == pid,
                   self.parsed_problems['result']['problems']))
        if len(r) != 1 and not self.up_to_date:
            self.update()
            return self.get_problem(contest_id, pid)
        if len(r) != 1:
            return None
          
        p = Problem(contest_id, pid, r[0]['name'], None,
                    "http://codeforces.com/contest/" + str(contest_id) +
                    "/problem/" + pid)
        # get test cases
        try:
            html = urlopen(p.url.encode('utf-8')).read()
        except:
            print "Could not get test cases for problem " + p.name
        parser = TestCasesHTMLParser()
        parser.feed(html)
        [p.add_test(t) for t in parser.tests]
        return p

    def get_contest(self, contest_id):
        if not self.contest_exists(contest_id, True) and not self.up_to_date:
            self.update()
        c = Contest(contest_id)
        [c.add_problem(self.get_problem(contest_id, p['index']))
         for p in list(filter(lambda x: x['contestId'] == contest_id,
                              self.parsed_problems['result']['problems']))]
        return c
