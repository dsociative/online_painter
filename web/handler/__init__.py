# coding: utf8

from engine.painter import Painter
from threading import Event
from tornado.web import RequestHandler
import json
import time


class BaseHandler(RequestHandler):

    painter = Painter()
    callbacks = set()

    def do_callbacks(self):
        for callback in self.callbacks:
            callback()

        BaseHandler.callbacks = set()

    def wait_action(self, callback):
        self.callbacks.add(callback)

    def cancel_wait(self, callback):
        self.callbacks.remove(callback)

    def canvas_json(self):
        return json.dumps(self.painter.canvas)
