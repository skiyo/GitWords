# -*- coding:utf8 -*-

import os

class Bag: pass

server = Bag()
server.port = 16890
server.process_num = 1

path = Bag()
path.static = os.path.join(os.path.dirname(__file__), "static")
