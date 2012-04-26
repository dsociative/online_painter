# coding: utf8

from engine.painter import Painter
from engine.tool.circle import Circle
from engine.tool.point import Point
from engine.toolkit import ToolKit
from ztest import ZTest


class PainterTest(ZTest):

    def setUp(self):
        self.painter = Painter()

    def test_init(self):
        self.isinstance(self.painter.kit, ToolKit)

    def test_do(self):
        x, y = 100, 100
        x2, y2 = 100, 40

        self.painter.do(Circle.id, (x, y), (x2, y2))
        self.eq(len(self.painter.items), 1)
        tool = self.painter.items[0]
        self.isinstance(tool, Circle)
        self.isinstance(tool.point, Point)
        self.eq(tool.point.x, x)
        self.eq(tool.point.y, y)
        self.eq(tool.point.y, y)

        self.eq(self.painter.canvas, [tool.ident()])
