# -*- coding:utf8 -*-

from pyoauth2 import Client
import conf

class Github:

	def __init__(self):
		self.client = Client(conf.github.app.client_id, conf.github.app.client_secret, 
			authorize_url = conf.github.api.authorize_url,
			token_url = conf.github.api.access_token_url)

	def authorize(self):
		return self.client.auth_code.authorize_url(scope = conf.github.app.scope)