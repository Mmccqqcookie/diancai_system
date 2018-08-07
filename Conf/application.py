#/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web
from Conf.settings import settings
from Conf.urls import urls


application = tornado.web.Application(urls,**settings)
