#!/usr/bin/python

try:
    from urllib2 import urlopen
    import json
except ImportError:
    print ImportError

import os
from Contest import Contest
from Problem import Problem


class CodeForces:

    def __init__(self, contest_db_path='contests', problem_db_path='problems'):
        self.up_to_date = False
        self.contests_path = contest_db_path
        self.problems_path = problem_db_path
        self.load_all_contests()
        self.load_all_problems()

    def load_all_contests(self, update=False):
        if update and os.path.isfile(self.contests_path):
            os.remove(self.contests_path)
        try:
            self.contests = open(self.contests_path).read()
        except:
            try:
                print "downloading contests..."
                self.contests = \
                    urlopen("http://codeforces.com/api/contest.list").read()
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
        if update and os.path.isfile(self.problems_path):
            os.remove(self.problems_path)
        try:
            self.problems = open(self.problems_path).read()
        except:
            try:
                print "downloading problems..."
                self.problems = \
                    urlopen(
                        "http://codeforces.com/api/problemset.problems").read()
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
        r = list(
            filter(lambda x: x['contestId'] == contest_id and x['index'] == pid,
                   self.parsed_problems['result']['problems']))
        if len(r) != 1 and not self.up_to_date:
            self.update()
            return self.get_problem(contest_id, pid)
        if len(r) != 1:
            return None
        return Problem(contest_id, pid, r[0]['name'], None,
                       'http://codeforces.com/contest/' + str(contest_id) +
                       '/problem/' + pid)

    def get_contest(self, contest_id):
        if not self.contest_exists(contest_id, True) and not self.up_to_date:
            self.update()
        c = Contest(contest_id)
        [c.add_problem(self.get_problem(contest_id, p['index']))
         for p in list(filter(lambda x: x['contestId'] == contest_id,
                              self.parsed_problems['result']['problems']))]
        return c
