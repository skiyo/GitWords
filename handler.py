# -*- coding:utf8 -*-
import tornado.web
from pyoauth2 import Client
import conf

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		print "aaa"
		#self.render("home.html", entries=entries)


class GithubOauthHandler(tornado.web.RequestHandler):
	def get(self):
		client = Client(conf.github.app.client_id, conf.github.app.client_secret, 
			authorize_url = conf.github.api.authorize_url, 
			token_url = conf.github.api.access_token_url)
		self.redirect(client.auth_code.authorize_url(scope = conf.github.app.scope))

class GithubCallbackHandler(tornado.web.RequestHandler):
	def get(self):
		client = Client(conf.github.app.client_id, conf.github.app.client_secret, 
			authorize_url = conf.github.api.authorize_url, 
			token_url = conf.github.api.access_token_url)
		self.write(self.get_argument('code'))
		access_token = client.auth_code.get_token(self.get_argument('code'), parse = "query")
		print 'token', access_token.headers


class PageNotFoundHandler(tornado.web.RequestHandler):
	def get(self):
		print "bbb"