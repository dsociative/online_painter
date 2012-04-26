# coding: utf8

from engine.tool import Tool
from ztest import ZTest


class ToolTest(ZTest):

    def test_ident(self):
        t = Tool((100, 100), 50)
        t.assign(0)

        self.eq(t.ident(), (0, ((100, 100))))
