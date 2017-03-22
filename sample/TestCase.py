#!/usr/bin/python

# Copyright 2017 Fabio Lima and Filipe CN

# class to store input and output of the problem


class TestCase:

    # construct of class testcase
    def __init__(self, input_text, output_text):
        self.input_text = input_text
        self.output_text = output_text
        self.problem = None

    # add problem in attribute
    def add_problem(self, problem):
        self.problem = problem
