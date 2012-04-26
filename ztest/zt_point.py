# coding: utf8

from engine.tool.point import Point
from ztest import ZTest


class PointTest(ZTest):

    def test_ident(self):

        p1 = Point(0, 50)
        p2 = Point(10, 20)

        p_delta = p1 - p2
        self.eq(p_delta.x, -10)
        self.eq(p_delta.y, 30)
        self.eq(p_delta.length, 31)

        self.eq(p_delta.ident(), (-10, 30))

