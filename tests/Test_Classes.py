#!/usr/bin/py
'''
Copyright 2017 Fabio Lima and Filipe CN

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
from sample.Entity import Entity
from sample.Problem import Problem
from sample.Contest import Contest
from sample.TestCase import TestCase


class TestClasses(unittest.TestCase):

    def test_init(self):
        entity_test = Entity('1', 'foo')
        self.assertEqual(str(entity_test.__class__), "sample.Entity.Entity")

    def test_problem_init(self):
        problem_test = Problem('3', 'bar', 'description', 'www.codeforces.com')
        self.assertEqual(str(problem_test.__class__), "sample.Problem.Problem")

    def test_contest_init(self):
        contest_test = Contest('2', 'wii')
        self.assertEqual(str(contest_test.__class__), "sample.Contest.Contest")

    def test_case_test_init(self):
        case_test = TestCase('input', 'output')
        self.assertEqual(str(case_test.__class__),
                         "sample.TestCase.TestCase")

    def test_problem_add_contest(self):
        problem_test = Problem('4', 'zoo', 'description', 'www.codeforces.com')
        contest_test = Contest('3', 'contest')
        problem_test.add_contest(contest_test)
        self.assertAlmostEqual(problem_test.contest.name, 'contest')

    def test_contest_add_problem(self):
        contest_test = Contest('5', 'contest')
        problem_1 = Problem('1', 'codeforces', 'description',
                            'www.codeforces.com')
        problem_2 = Problem('2', 'topcoder', 'description', 'www.topcoder.com')
        contest_test.add_problem(problem_1)
        contest_test.add_problem(problem_2)
        self.assertEqual(contest_test.problem_list[1].name, 'topcoder')

    def test_test_case_add_test(self):
        problem_test = Problem('4', 'zoo', 'description', 'www.codeforces.com')
        case_test = TestCase('3', 'test')
        case_test.add_problem(problem_test)
        self.assertEqual(case_test.problem.name, 'zoo')

if __name__ == "__main__":
    unittest.main()
