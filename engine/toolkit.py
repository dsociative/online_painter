# coding: utf8

from engine.tool.circle import Circle
from engine.tool.line import Line


class ToolKit(object):

    tools = [Circle, Line]

    def __init__(self):
        self.calculate()

    def __getitem__(self, index):
        return self.tools[index]

    def calculate(self):
        for no, tool in enumerate(self.tools):
            tool.assign(no)

