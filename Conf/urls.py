#/usr/bin/env python
#-*- coding:utf-8 -*-
from views import *


urls = [
    ('/',IndexHandler),
    ('/search_keyword',SearchKeywordHandler),
    ('/send_email_code',Send_EmailHandler),
    ('/resgistr',ResgistrHandler),
    ('/login',LoginHandler),
    ('/logout',LogoutHandler),
    ('/add_dish_menu',AddDishMenuHandler),
    ('/category/(\d+.*)',PageTabHandler),
    ('/suiji_dish',SuijiDishNumHandler),
]