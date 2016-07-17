# coding: utf-8
from tornado.web import RequestHandler as BaseHandler
import textwrap


class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html")


class PoemPageHandler(BaseHandler):
    def post(self):
        noun1 = self.get_argument("noun1")
        noun2 = self.get_argument("noun2")
        verb = self.get_argument("verb")
        noun3 = self.get_argument("noun3")
        self.render("poem.html", roads=noun1, wood=noun2, made=verb, difference=noun3)


class ReverseHandler(BaseHandler):
    def get(self, word):
        self.write(word[::-1])


class WrapHandler(BaseHandler):
    def post(self):
        text = self.get_argument("text")
        width = self.get_argument("width", 40)
        self.write(textwrap.fill(text, int(width)))


class AlgorithmDemoFormHandler(BaseHandler):
    def get(self):
        self.render("demo_form.html")


class AlgorithmDemoHandler(BaseHandler):
    def prepare(self):
        item1_id = self.get_argument("item1_id")
        item2_id = self.get_argument("item2_id")
        self.render("demo.html", item1_id=item1_id, item2_id=item2_id)