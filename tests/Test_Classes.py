#!/usr/bin/py

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
from sample.Entity import Entity
from sample.Problem import Problem


class TestClasses(unittest.TestCase):

    def test_init(self):
        entity_test = Entity('1', 'foo')
        self.assertEqual(str(entity_test.__class__), "sample.Entity.Entity")

    def test_problem(self):
        problem_test = Problem('3', 'bar', 'description', 'www.codeforces.com')
        self.assertAlmostEqual(str(problem_test.__class__),
                               "sample.Problem.Problem")
if __name__ == "__main__":
    unittest.main()
