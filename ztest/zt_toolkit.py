# coding: utf8

from engine.tool.circle import Circle
from engine.toolkit import ToolKit
from ztest import ZTest


class PainterTest(ZTest):

    def test_init(self):
        kit = ToolKit
        self.eq(kit.tools[0], Circle)
        kit = ToolKit()
        self.eq(kit.tools[0].id, kit.tools.index(Circle))

