# -*- coding:utf8 -*-
import tornado.web
from pyoauth2 import Client
import conf
from model.github import Github

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		print "aaa"
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
		"""
		client = Client(conf.github.app.client_id, conf.github.app.client_secret, 
			authorize_url = conf.github.api.authorize_url, 
			token_url = conf.github.api.access_token_url)
		access_token = client.auth_code.get_token(self.get_argument('code'), parse = "query")
		print 'token', access_token.headers
		ret = access_token.get('https://api.github.com/user')
		print ret.parsed
		"""


class PageNotFoundHandler(tornado.web.RequestHandler):
	def get(self):
		print "bbb"