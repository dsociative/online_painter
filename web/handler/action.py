# coding: utf8

from web.handler import BaseHandler
import json


class Action(BaseHandler):

    def post(self):
        tool_id = self.get_argument('id')
        args = self.get_argument('args')
        self.painter.do(int(tool_id), *json.loads(args))

        return self.do_callbacks()
