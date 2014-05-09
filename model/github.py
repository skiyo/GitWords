# -*- coding:utf8 -*-

from pyoauth2 import Client
from pyoauth2.libs.access_token import AccessToken
import conf
import base64

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

	def get_user_repos(self):
		return self.access_token.get(conf.github.api.repos_get_url).parsed

	def check_repos(self):
		return not (conf.gitwords.app.repos_name in self.get_user_repos())

	def create_repos(self, name = conf.gitwords.app.repos_name):
		return self.access_token.post(conf.github.api.repos_add_url,
			name = name, has_issues = False, has_wiki = False, 
			has_downloads = False, headers = {'content-type' : 'application/json'}).parsed

	def create_file(self, user, filename, content):
		return self.access_token.put(self._parse_api_url(conf.github.api.create_file, 
			owner = user, repo = conf.gitwords.app.repos_name, path = filename), 
			path = filename, message = conf.github.api.update_message, content = base64.b64encode(content),
			branch = conf.github.api.branch, headers = {'content-type' : 'application/json'}).parsed
		"""
		return self.access_token.put('https://api.github.com/repos/skiyo/_gitwords/contents/CNAME', 
			path = 'CNAME', message = 'message', content = base64.b64encode('blog-sample.verycoder.com'), 
			branch = 'gh-pages', headers = {'content-type' : 'application/json'}).parsed
		"""

	def _parse_api_url(self, url, **param):
		for key in param:
			url = url.replace(":%s" % k, str(opts[k]))
		return url
