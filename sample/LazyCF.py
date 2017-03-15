#!/usr/bin/python

# Copyright 2017 Fabio Lima and Filipe CN

import os
import sys
import argparse
from CodeForces import CodeForces


class LazyCF():

    def __init__(self):
        self.contest = None

    def get_contest(self, id_contest):
        code_forces = CodeForces()
        self.contest = code_forces.get_contest(int(id_contest))

    def verify_args(self, args):
        self.get_contest(args)

    def create_folder(self, contest, path=None):
        if path is None:
            path = os.getcwd()
        for problem in contest.problem_list:
            try:
                os.mkdir(path + "/" + problem.index)
            except OSError:
                print "could not create folder " + problem.index

    def create_file(self, case_test, problem_name, path=None):
        if path is None:
            path = os.getcwd()
        path += '/' + problem_name
        try:
            f_descriptor = open(path, "w+")
            f_descriptor.write(case_test)
        except OSError:
            print "could not create a file " + case_test.name


if __name__ == '__main__':
    execute = LazyCF()
    parse = argparse.ArgumentParser()
    parse.add_argument("contest", type=int,
                       help="it's necessary contest id to run")
    args = parse.parse_args()
    if (len(sys.argv) == 1) or \
       (len(sys.argv) == 2 and
        (sys.argv[1] == "-h" or
         sys.argv[1] == "--help")):
        print args.contest
    elif len(sys.argv) > 1:
        execute.verify_args(sys.argv[1])
        execute.create_folder(execute.contest)
