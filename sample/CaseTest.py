#!/usr/bin/py


class CaseTest:

    def __init__(self, input_text, output_text):
        self.input_text = input_text
        self.output_text = output_text
        self.problem = None

    def add_problem(self, problem):
        self.problem = problem
