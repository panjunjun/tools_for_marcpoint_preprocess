# coding: utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from router import handler, template_path
define(u"port", default=8188, help="run on given port", type=int)


if __name__ == u"__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=handler, template_path=template_path, debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print ("web server start")
    tornado.ioloop.IOLoop.instance().start()
