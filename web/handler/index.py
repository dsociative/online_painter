# coding: utf8

from web.handler import BaseHandler


class Index(BaseHandler):

    def get(self):
        return self.render('index.html')
