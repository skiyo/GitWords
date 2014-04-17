# -*- coding:utf8 -*-

import os

class Bag: pass

server = Bag()
server.port = 80
server.process_num = 1

github = Bag()
github.app = Bag()
github.app.client_id = 'd6fac7621e36041c249e'
github.app.client_secret = 'c724416ce67c5d9440bb891c05e35f91c22d375c'
github.app.scope = 'user,public_repo,gist'

github.api = Bag()
github.api.authorize_url = 'https://github.com/login/oauth/authorize'
github.api.access_token_url = 'https://github.com/login/oauth/access_token'

tornado_settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "static"),
	xsrf_cookies = True,
	cookie_secret = "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
	login_url = "/github/oauth",
	debug = True,
)