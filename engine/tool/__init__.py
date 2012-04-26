# coding: utf8


class Tool(object):

    @classmethod
    def assign(cls, value):
        cls.id = value
        return cls

    def __init__(self, point, radius):
        self.point = point
        self.radius = radius

    def ident(self):
        return self.id, (self.point, self.radius)
