#!/usr/bin/env python2.7
# coding: utf8

from lib.tornado_daemon import TornadoDaemon
from tornado.web import url, Application
from web.handler.action import Action
from web.handler.index import Index
from web.handler.pooling import Pooling
from os.path import abspath


urls = [url(r'/', Index, name='index'),
        url(r'/pooling', Pooling, name='pooling'),
        url(r'/action', Action, name='action'), ]

app = Application(urls, template_path=abspath('web/template'),
                  static_path=abspath('web/static'))


if __name__ == '__main__':
    service = TornadoDaemon(app, 8888, '/tmp/online_painter.pid',
                            stderr=abspath('error.log'))

    if service.process_argv():
        pass
    else:
        service.run()
