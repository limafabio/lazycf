#!/usr/bin/python

# Copyright 2017 Fabio Lima and Filipe CN

from Entity import Entity

# class to store problem


class Problem(Entity):

    # construct of class problem
    def __init__(self, contest_id, index, name, description, url):
        Entity.__init__(self, str(contest_id) + index, name)
        self.description = description
        self.url = url
        self.contest = None
        self.test = []
        self.index = index
        self.contest_id = contest_id

    # add contest in attribute
    def add_contest(self, contest):
        self.contest_id = contest

    # add test in attribute
    def add_test(self, test):
        self.test.append(test)
