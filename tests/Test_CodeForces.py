#!/usr/bin/python

# Copyright 2017 Fabio Lima and Filipe CN

import json
import os
import sys
import unittest
from sample.CodeForces import CodeForces
sys.path.append(os.path.abspath('..'))


class TestCodeForces(unittest.TestCase):

    def test_init(self):
        cf = CodeForces()
        self.assertEqual(str(cf.__class__), "sample.CodeForces.CodeForces")
        self.assertTrue(os.path.isfile(cf.contests_path))
        self.assertTrue(os.path.isfile(cf.problems_path))
        self.assertTrue(cf.parsed_contests['status'] == 'OK')
        self.assertTrue(cf.parsed_problems['status'] == 'OK')

    def test_update(self):
        cf = CodeForces()
        self.assertFalse(cf.up_to_date)
        cf.update()
        self.assertTrue(cf.up_to_date)

    def test_contest_exists(self):
        cf = CodeForces()
        cf.up_to_date = True
        self.assertTrue(cf.contest_exists(768))
        self.assertTrue(cf.contest_exists(768, True))
        self.assertFalse(cf.contest_exists(-1))
        self.assertFalse(cf.contest_exists(-1, True))
        # delete problems
        cf.parsed_problems['result']['problems'] = \
            [item for item in cf.parsed_problems['result']['problems']
             if item['contestId'] != 768]
        self.assertTrue(cf.contest_exists(768))
        self.assertFalse(cf.contest_exists(768, True))
        self.assertTrue(cf.up_to_date)
        cf.up_to_date = False
        self.assertTrue(cf.contest_exists(768, True))
        self.assertTrue(cf.up_to_date)
        # delete contest
        cf.parsed_contests['result'] = \
            [item for item in cf.parsed_contests['result']
             if item['id'] != 773]
        cf.up_to_date = True
        self.assertFalse(cf.contest_exists(773))
        cf.up_to_date = False
        self.assertTrue(cf.contest_exists(773))
        self.assertTrue(cf.up_to_date)

    def check_problem(self, p, o):
        self.assertTrue(p.index == o['index'])
        self.assertTrue(p.contest_id == o["contestId"])
        self.assertTrue(p.id == str(o['contestId']) + o['index'])
        self.assertTrue(p.description is None)
        self.assertTrue(p.name == o["name"])
        self.assertTrue(p.url == 'http://codeforces.com/contest/' +
                        str(o['contestId']) + '/problem/' + o['index'])

    def test_get_problem(self):
        cf = CodeForces()
        p = cf.get_problem(768, "G")
        o = json.loads('{"contestId":768,"index":"G",\
                       "name":"The Winds of Winter", "type":"PROGRAMMING",\
                       "points":2750.0,"tags":["data structures"]}')
        self.check_problem(p, o)
        # delete problems
        cf.parsed_problems['result']['problems'] = \
            [item for item in cf.parsed_problems['result']['problems']
             if item['contestId'] != 768]
        cf.up_to_date = True
        p = cf.get_problem(768, "G")
        self.assertTrue(p is None)
        cf.up_to_date = False
        p = cf.get_problem(768, "G")
        self.assertTrue(cf.up_to_date)
        self.check_problem(p, o)

    def check_contest(self, c, o, problems):
        self.assertTrue(c.id == o['id'])
        self.assertTrue(len(c.problem_list) == len(problems))
        for problem in c.problem_list:
            self.check_problem(problem, list(filter(lambda x: x['index'] ==
                                                    problem.index,
                                                    problems))[0])

    def test_get_contest(self):
        cf = CodeForces()
        c = cf.get_contest(768)
        co = json.loads('{"id":768,"name":"Divide by Zero 2017 and Codeforces \
                       Round #399 (Div. 1 + Div. 2, combined)","type":"CF",\
                       "phase":"FINISHED","frozen":false,"durationSeconds":\
                       9600,"startTimeSeconds":1487606700,\
                       "relativeTimeSeconds":90744}')
        cp = json.loads('[{"contestId":768,"index":"G",\
                        "name":"The Winds of Winter","type":"PROGRAMMING",\
                        "points":2750.0,"tags":\
                        ["data structures"]},{"contestId":768,"index":"F",\
                        "name":"Barrels and boxes","type":"PROGRAMMING",\
                        "points":2250.0,"tags":["brute force","combinatorics",\
                        "number theory","probabilities"]},{"contestId":768,\
                        "index":"E","name":"Game of Stones","type":\
                        "PROGRAMMING","points":2000.0,"tags":["dp","games"]},\
                        {"contestId":768,"index":"D","name":"Jon and Orbs",\
                        "type":"PROGRAMMING","points":1750.0,"tags":["dp",\
                        "math","probabilities"]},{"contestId":768,"index":"C",\
                        "name":"Jon Snow and his Favourite Number","type":\
                        "PROGRAMMING","points":1250.0,"tags":["brute force",\
                        "dp","implementation","sortings"]},{"contestId":768,\
                        "index":"B","name":"Code For 1","type":"PROGRAMMING",\
                        "points":1000.0,"tags":["constructive algorithms",\
                        "dfs and similar","divide and conquer"]},\
                        {"contestId":768,"index":"A",\
                        "name":"Oath of the Night\u0027s Watch",\
                        "type":"PROGRAMMING","points":\
                        500.0,"tags":["constructive algorithms",\
                        "sortings"]}]')
        self.check_contest(c, co, cp)
        cf.parsed_problems['result']['problems'] = \
            [item for item in cf.parsed_problems['result']['problems']
             if item['contestId'] != 768]
        cf.up_to_date = True
        c = cf.get_contest(768)
        self.assertTrue(len(c.problem_list) == 0)
        cf.up_to_date = False
        c = cf.get_contest(768)
        self.check_contest(c, co, cp)
        self.assertTrue(cf.up_to_date)
        self.assertTrue(len(c.problem_list) == 7)

    def test_get_problem_test_cases(self):
        cf = CodeForces()
        p = cf.get_problem(768, "G")
        inputs = []
        inputs.append(open("aux/test_case_input", "r").read())
        inputs.append(open("aux/test_case_input_1", "r").read())
        outputs = []
        outputs.append(open("aux/test_case_output", "r").read())
        outputs.append(open("aux/test_case_output_1", "r").read())
        for i in range(2):
            print "checking case test " + p.test[i].input_text
            self.assertEquals(p.test[i].input_text, inputs[i])
            self.assertEquals(p.test[i].output_text, outputs[i])

if __name__ == "__main__":
    unittest.main()
