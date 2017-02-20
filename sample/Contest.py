#!/usr/bin/py

from Entity import Entity


class Contest(Entity):

    def __init__(self, id_obj, name):
        Entity.__init__(self, id_obj, name)
