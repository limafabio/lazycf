#!/usr/bin/python

# Copyright 2017 Fabio Lima and Filipe CN

from Entity import Entity

# class that store contest with set of problems


class Contest(Entity):

    # construct of the class contest
    def __init__(self, id_obj):
        Entity.__init__(self, id_obj, None)
        self.problem_list = []

    # add a problem in problem list
    def add_problem(self, problem):
        self.problem_list.append(problem)
