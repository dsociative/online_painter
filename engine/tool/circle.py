# coding: utf8

from engine.tool import Tool
from engine.tool.point import Point


class Circle(Tool):

    def init(self, xy2):
        self.radius = (Point(*xy2) - self.point).length

    def ident(self):
        return self.id, (self.point.ident(), self.radius)
