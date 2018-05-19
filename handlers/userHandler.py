# coding=utf-8

import tornado.web

import json

import methods.userMethod

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(methods.userMethod.queryAll()))