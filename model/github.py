# -*- coding:utf8 -*-

from pyoauth2 import Client
from pyoauth2.libs.access_token import AccessToken
import conf

class Github:

	def __init__(self, access_token = ''):
		self.client = Client(conf.github.app.client_id, conf.github.app.client_secret, 
			authorize_url = conf.github.api.authorize_url,
			token_url = conf.github.api.access_token_url)
		if len(access_token) > 0:
			self.access_token = AccessToken(self.client, access_token, parse = "query")

	def authorize(self):
		return self.client.auth_code.authorize_url(scope = conf.github.app.scope)

	def set_code(self, code):
		if self.access_token:
			return
		self.access_token = self.client.auth_code.get_token(code, parse = "query")

	def get_user_info(self):
		return self.access_token.get(conf.github.api.user_get_url).parsed

