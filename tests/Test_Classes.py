#!/usr/bin/py

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
from sample.Entity import Entity
from sample.Contest import Contest


class TestClasses(unittest.TestCase):

    def test_init(self):
        entity_test = Entity('1', 'foo')
        self.assertEqual(str(entity_test.__class__), "sample.Entity.Entity")

    def test_contest(self):
        contest_test = Contest('2', 'bar')
        self.assertEqual(str(contest_test.__class__), "sample.Contest.Contest")

if __name__ == "__main__":
    unittest.main()
