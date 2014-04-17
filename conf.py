# -*- coding:utf8 -*-

import os

class Bag: pass

server = Bag()
server.port = 80
server.process_num = 1

path = Bag()
path.static = os.path.join(os.path.dirname(__file__), "static")

tornado_settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "static"),
	xsrf_cookies = True,
	cookie_secret = "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
	login_url = "/github/oauth",
	debug = True,
)