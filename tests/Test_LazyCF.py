#!/usr/bin/python

# Copyright 2017 Fabio Lima and Filipe CN

import os
import sys
import shutil
import unittest
from sample.LazyCF import LazyCF
from sample.CodeForces import CodeForces
sys.path.append(os.path.abspath('..'))


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

    def test_create_file(self):
        cf = CodeForces()
        contest_test = cf.get_contest(768)
        lazy = LazyCF()
        lazy.create_folder(contest_test)
        path = os.path.abspath('.')

        for folder in contest_test.problem_list:
            path_folder = path + "/" + folder.index
            self.assertTrue(os.path.isdir(path_folder))
            i = 0
            for cases in folder.test:
                i += 1
                name_file = "input_" + str(i)
                lazy.create_file(cases.input_text, name_file, path_folder)
                name_file = "output_" + str(i)
                lazy.create_file(cases.output_text, name_file, path_folder)
            shutil.rmtree(path_folder)


if __name__ == "__main__":
    unittest.main()
