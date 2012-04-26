# coding: utf8

from engine.painter import Painter
from engine.tool.circle import Circle
from engine.toolkit import ToolKit
from ztest import ZTest


class PainterTest(ZTest):

    def setUp(self):
        self.painter = Painter()

    def test_init(self):
        self.isinstance(self.painter.kit, ToolKit)

    def test_do(self):
        point = (100, 100)
        radius = 40

        self.painter.do(Circle.id, point, radius)
        self.eq(len(self.painter.items), 1)
        tool = self.painter.items[0]
        self.isinstance(tool, Circle)
        self.eq(tool.point, point)
        self.eq(self.painter.canvas, [tool.ident()])
