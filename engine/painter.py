# coding: utf8

from engine.toolkit import ToolKit


class Painter(object):

    def __init__(self):
        self.kit = ToolKit()
        self.items = []

    def do(self, tool_id, point, *args, **kw):
        tool = self.kit[tool_id](point, *args, **kw)
        self.append(tool)

    def append(self, item):
        self.items.append(item)

    def gen_canvas(self):
        for item in self.items:
            yield item.ident()

    @property
    def canvas(self):
        return list(self.gen_canvas())

