# coding: utf8

from engine.tool.line import Line
from ztest import ZTest


class LineTest(ZTest):

    def setUp(self):
        Line.assign(0)

    def test_ident(self):
        t = Line((100, 100), (100, 40))
        self.eq(t.ident(), (0, (t.point.ident(), t.end.ident())))

