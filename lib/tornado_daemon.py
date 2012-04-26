# coding: utf8

from daemon import Daemon
import sys
import tornado.httpserver
import tornado.ioloop


IOLoop = tornado.ioloop.IOLoop
HTTPServer = tornado.httpserver.HTTPServer


def command_line_first_arg_is(word):
    if len(sys.argv) < 2:
        return False
    return word == sys.argv[1]


### Запуск сервера


class TornadoDaemon(Daemon):
    ''' Базовый класс для запуска Торнадо как автозагружаемого скрипта '''

    app_name = 'Tornado Daemon Base'

    smart_dev = True
    debug_mode = command_line_first_arg_is('dev')

    def __init__(self, application, port, *args, **kwargs):
        self.app = application
        self.port = port
        Daemon.__init__(self, *args, **kwargs)

    def init_run(self):
        pass

    def run(self):
        ''' Создать app и запустить ioloop '''
        self.init_run()
        self.server(self.app).listen(self.port)
        self.start_ioloop()

    def server(self, app, server=HTTPServer, **kw):
        if self.debug_mode:
            app.settings['debug'] = True
        return server(app, **kw)

    @property
    def ioloop(self):
        return IOLoop.instance()

    def start_ioloop(self):
        self.ioloop.start()

    def stop(self):
        try:
            self.ioloop.stop()
        finally:
            Daemon.stop(self)

    def process_command_line(self):
        if command_line_first_arg_is('start'):
            self.start()
        elif command_line_first_arg_is('stop'):
            self.stop()
        elif command_line_first_arg_is('restart'):
            self.restart()
        elif command_line_first_arg_is('dev') or self.smart_dev:
            self.debug_mode = True
            self.run()
        else:
            print "%s usage: %s start|stop|restart|dev" % (self.app_name,
                                                           sys.argv[0])
            sys.exit(2)
            return self
        sys.exit(0)
        return self
