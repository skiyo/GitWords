# -*- coding:utf8 -*-

import tornado.web
import conf
import handler

controller = [
	(r"/", handler.IndexHandler),
	(r"/github/oauth", handler.GithubOauthHandler),
	(r"/github/callback", handler.GithubCallbackHandler),
	(r".*", handler.PageNotFoundHandler),
]