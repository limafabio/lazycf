#!/usr/bin/py

from Entity import Entity


class Contest(Entity):

    def __init__(self, id_obj):
        Entity.__init__(self, id_obj, None)
        self.problem_list = []

    def add_problem(self, problem):
        self.problem_list.append(problem)
