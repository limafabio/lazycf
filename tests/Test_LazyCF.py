#!/usr/bin/py

import os
import sys
import shutil
import unittest
sys.path.append(os.path.abspath('..'))
from sample.LazyCF import LazyCF
from sample.CodeForces import CodeForces


class TestLazyCF(unittest.TestCase):

    def test__init__(self):
        lazy_test = LazyCF()
        self.assertEqual(str(lazy_test.__class__), "sample.LazyCF.LazyCF")

    def test_get_contest(self):
        cf = LazyCF()
        cf.get_contest(768)
        self.assertEqual(cf.contest.id, 768)

    def test_create_folder(self):
        cf = CodeForces()
        contest_test = cf.get_contest(768)
        lazy = LazyCF()
        lazy.create_folder(contest_test)
        path = os.path.abspath('.')
        for folder in contest_test.problem_list:
            self.assertTrue(os.path.isdir(path + "/" + folder.index))
            shutil.rmtree(path + "/" + folder.index)


    '''
    def test_create_file(self):
        cf = CodeForces()
        contest_test = cf.get_contest(768)
        lazy = LazyCF()
        lazy.create_folder(contest_test)
        path = os.path.abspath('.')
        path += "/" + contest_test.problem_list[0].index
        print "EH o bicho " + str(len(contest_test.problem_list[0].test))
        lazy.create_file(contest_test.problem_list[0].test[0],
                         contest_test.problem_list[0], path)

    '''
if __name__ == "__main__":
    unittest.main()
