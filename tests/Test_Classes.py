#!/usr/bin/py

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
from sample.Entity import Entity

class TestClasses(unittest.TestCase):

    def test_init(self):
        entity_test = Entity('1', 'foo')
        self.assertEqual(str(entity_test.__class__), "sample.Entity.Entity")

if __name__ == "__main__":
    unittest.main()
