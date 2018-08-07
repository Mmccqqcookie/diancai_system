#/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.ioloop
from Conf.application import application


if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()