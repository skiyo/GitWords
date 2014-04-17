# -*- coding:utf8 -*-

import tornado.ioloop
import tornado.web
import router
import conf
import os
import sys

if __name__ == "__main__" :

	reload(sys)
	sys.setdefaultencoding('utf-8')

	app = tornado.web.Application(router.controller)
	server = HTTPServer(app)
	server.bind(conf.server.port)
	server.start(conf.server.process_num)

	tornado.ioloop.IOLoop.instance().start()