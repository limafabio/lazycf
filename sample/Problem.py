#!/usr/bin/py

from Entity import Entity


class Problem(Entity):

    def __init__(self, contest_id, index, name, description, url):
        Entity.__init__(self, str(contest_id) + index, name)
        self.description = description
        self.url = url
        self.contest = None
        self.test = []
        self.index = index
        self.contest_id = contest_id

    def add_contest(self, contest):
        self.contest_id = contest

    def add_test(self, test):
        self.test.append(test)
