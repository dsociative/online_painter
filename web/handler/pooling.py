# coding: utf8

from tornado.web import asynchronous
from web.handler import BaseHandler


class Pooling(BaseHandler):

    def get(self):
        return self.finish(self.canvas_json())

    def on_action(self):
        return self.finish(self.canvas_json())

    @asynchronous
    def post(self):
        self.wait_action(self.on_action)

    def on_connection_close(self):
        self.cancel_wait(self.on_action)
