# coding: utf-8
import tornado.httpserver as httpserver
import tornado.ioloop as ioloop
import tornado.web
from tornado.options import define, options
from router import handler, template_path
define("port", default=8188, help="run on given port", type=int)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=handler, template_path=template_path)
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print ("web server start")
    ioloop.IOLoop.instance().start()
