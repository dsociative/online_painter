# coding: utf8

import math


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)

    @property
    def length(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def ident(self):
        return self.x, self.y
