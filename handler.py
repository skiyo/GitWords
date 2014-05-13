# -*- coding:utf8 -*-
import tornado.web
from pyoauth2 import Client
import conf
from model.github import Github

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		g = Github('591ec9909c3330223cc4e988f61b0c5d4ee17800')
		#print g.get_user_info()
		#print g.check_repos()

		print g.update_file('skiyo', 'test.html', "bbbb", 'f2ba8f84ab5c1bce84a7b441cb1959cfc7093b7f')
		if self.get_secure_cookie('u'):
			self.write(self.get_secure_cookie('u'))
		else :
			self.write('not login')
		#self.render("home.html", entries=entries)


class GithubOauthHandler(tornado.web.RequestHandler):
	def get(self):
		g = Github()
		self.redirect(g.authorize())

class GithubCallbackHandler(tornado.web.RequestHandler):
	def get(self):
		g = Github()
		g.set_code(self.get_argument('code'))
		user = g.get_user_info()
		self.set_secure_cookie('u', user['login'])


class PageNotFoundHandler(tornado.web.RequestHandler):
	def get(self):
		print "PageNotFound"