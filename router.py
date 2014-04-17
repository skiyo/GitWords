# -*- coding:utf8 -*-

import action
import tornado.web
import conf

controller = [
	(r"/", IndexHandler),

	(r"/static/(.*)", tornado.web.StaticFileHandler, {"path": conf.path.static}),
]