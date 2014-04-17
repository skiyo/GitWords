# -*- coding:utf8 -*-

import tornado.web
import conf
import handler

controller = [
	(r"/", handler.IndexHandler),
]

tornado.web.ErrorHandler = handler.PageNotFoundHandler