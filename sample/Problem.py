#!/usr/bin/py

from Entity import Entity


class Problem(Entity):

    def __init__(self, id_obj, name, description, url):
        Entity.__init__(self, id_obj, name)
        self.description = description
        self.url = url
        self.contest = None
        self.test = []

    def add_contest(self, contest):
        self.contest = contest

    def add_test(self, test):
        self.test.append(test)
