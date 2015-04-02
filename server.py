# -*- coding: utf-8 -*-
import os
import tornado.ioloop
import tornado.web
import api.chat
import api.love

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("list.html")

class ChatHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("chat.html")

class APIChatHandler(tornado.web.RequestHandler):
    def get(self):
        message_id = self.get_argument("message_id")
        self.write(api.chat.get_message(message_id))

class APILoveHandler(tornado.web.RequestHandler):
    def get(self):
        love_value = self.get_argument("love_value")
        text = self.get_argument("text")
        self.write(api.love.get_love_value(love_value,text))

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/chat", ChatHandler),
    (r"/list", ListHandler),
    (r"/api/love", APILoveHandler),
    (r"/api/chat", APIChatHandler),
    ],debug=True,
    template_path=os.path.join(os.getcwd(),  "templates"),
    static_path=os.path.join(os.getcwd(),  "static"),
)

if __name__ == "__main__":
    application.listen(8000)
    print("Server is up ...")
    tornado.ioloop.IOLoop.instance().start()
