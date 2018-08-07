#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Author : hucheng-self
    @Time : 2018/8/4 16:31
"""
from Repository.CaimenuRepository import CaiMenuRepository
class Model_caiMenu:
    def __init__(self,id,title,url,img_url,side_dish,stats,category_id):
        self.id = id
        self.title = title
        self.url = url
        self.img_url = img_url
        self.side_dish = side_dish
        self.stats = stats
        self.category_id = category_id


class CaiMenuService:
    def __init__(self):
        self.repository = CaiMenuRepository()

    def check_dish_exits(self,title):
        result = self.repository.check_dish_exits(title)
        return result


    def add_dish(self,title,url,img_url,side_dish,stats,category_id):
        self.repository.add_dish(title,url,img_url,side_dish,stats,category_id)