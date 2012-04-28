# coding: utf8

from engine.tool.circle import Circle
from ztest import ZTest


class CircleTest(ZTest):

    def setUp(self):
        Circle.assign(0)

    def test_ident(self):
        t = Circle((100, 100), (100, 40))

        self.eq(t.radius, 60)
        self.eq(t.ident(), (0, (t.point.ident(), t.radius)))

