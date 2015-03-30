# -*- coding: utf-8 -*-
import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ChatHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("chat.html")

class FacebookHandler(tornado.web.RequestHandler):
    def get(self):
        response = {}
        self.write(response)

class LoveHandler(tornado.web.RequestHandler):
    def get(self):
        response = {}
        self.write(response)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/chat", ChatHandler),
    (r"/api/facebook", FacebookHandler),
    (r"/api/love", LoveHandler),
    ],debug=True,
    template_path=os.path.join(os.getcwd(),  "templates"),
    static_path=os.path.join(os.getcwd(),  "static"),
)

if __name__ == "__main__":
    application.listen(8888)
    print("Server is up ...")
    tornado.ioloop.IOLoop.instance().start()
