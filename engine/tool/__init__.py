# coding: utf8
from engine.tool.point import Point


class Tool(object):

    @classmethod
    def assign(cls, value):
        cls.id = value
        return cls

    def __init__(self, xy, *args, **kwargs):
        self.point = Point(*xy)
        self.init(*args, **kwargs)

    def init(self, *args, **kwargs):
        ''' personal tool init, override it '''

    def ident(self):
        return self.id, (self.point.ident())
