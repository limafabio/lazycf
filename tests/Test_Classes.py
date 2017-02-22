#!/usr/bin/py

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
from sample.Entity import Entity
from sample.Problem import Problem
from sample.Contest import Contest
from sample.CaseTest import CaseTest


class TestClasses(unittest.TestCase):

    def test_init(self):
        entity_test = Entity('1', 'foo')
        self.assertEqual(str(entity_test.__class__), "sample.Entity.Entity")

    def test_problem_init(self):
        problem_test = Problem('3', 'bar', 1, 'description',
                               'www.codeforces.com')
        self.assertEqual(str(problem_test.__class__), "sample.Problem.Problem")

    def test_contest_init(self):
        contest_test = Contest('2')
        self.assertEqual(str(contest_test.__class__), "sample.Contest.Contest")

    def test_case_test_init(self):
        case_test = CaseTest('input', 'output')
        self.assertEqual(str(case_test.__class__),
                         "sample.CaseTest.CaseTest")

    def test_problem_add_contest(self):
        problem_test = Problem('4', '1', 'zoo', 'description',
                               'www.codeforces.com')
        contest_test = Contest('3')
        problem_test.add_contest(contest_test)
        self.assertAlmostEqual(problem_test.contest_id.id, '3')

    def test_contest_add_problem(self):
        contest_test = Contest('5')
        problem_1 = Problem('1', '1', 'codeforces', 'description',
                            'www.codeforces.com')
        problem_2 = Problem('2', '2', 'topcoder', 'description',
                            'www.topcoder.com')
        contest_test.add_problem(problem_1)
        contest_test.add_problem(problem_2)
        self.assertEqual(contest_test.problem_list[1].contest_id, '2')

    def test_case_test_add_test(self):
        problem_test = Problem('4', '3', 'zoo', 'description',
                               'www.codeforces.com')
        case_test = CaseTest('input', 'output')
        case_test.add_problem(problem_test)
        self.assertEqual(case_test.problem.contest_id, '4')


if __name__ == "__main__":
    unittest.main()
