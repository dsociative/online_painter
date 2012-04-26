# coding: utf8

from engine.tool import Tool
from engine.tool.point import Point


class Line(Tool):

    def init(self, xy):
        self.end = Point(*xy)

    def ident(self):
        return self.id, (self.point.ident(), self.end.ident())
