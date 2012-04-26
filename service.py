#!/usr/bin/env python2.7
# coding: utf8

from lib.tornado_daemon import TornadoDaemon
from tornado.web import url, Application
from web.handler.action import Action
from web.handler.index import Index
from web.handler.pooling import Pooling

urls = [url(r'/', Index, name='index'),
        url(r'/pooling', Pooling, name='pooling'),
        url(r'/action', Action, name='action'), ]

app = Application(urls, template_path='web/template', static_path='web/static')


if __name__ == '__main__':
    service = TornadoDaemon(app, 8888, '/tmp/online_painter.pid')

    if service.process_argv():
        pass
    else:
        from tornado.httpserver import HTTPServer
        from tornado.ioloop import IOLoop
        srv = HTTPServer(app)
        srv.bind(8888, '192.168.1.10')
        srv.start(1)

        IOLoop.instance().start()
