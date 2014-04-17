# -*- coding:utf8 -*-
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		print "aaa"
		#self.render("home.html", entries=entries)


class PageNotFoundHandler(tornado.web.RequestHandler):
	def get(self):
		print "bbb"