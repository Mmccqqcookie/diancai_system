#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Author : hucheng-self
    @Time : 2018/8/4 17:10
"""
from Model.CaiMenu import CaiMenuService
from Service.caimenu.ModelView import model_view
from Service.caimenu.response import Response


class CaiMenu_Service:
    def __init__(self):
        self.response = Response()
        self.cai_menu_service = CaiMenuService()
        self.model = None


    def check_dish_exits(self,title):
        self.model = self.cai_menu_service.check_dish_exits(title)
        try:
            if self.model:
                modelview = model_view(id=self.model.id,title=self.model.title,
                                       url=self.model.url,img_url=self.model.img_url,
                                       side_dish=self.model.side_dish,stats=self.model.stats,
                                       category_id=self.model.category_id)

                self.response.model_view = modelview
            else:
                raise Exception('数据中，没有此菜！')

        except Exception as e:
            self.response.status = False
            self.response.message = str(e)

        return self.response

    def add_dish(self,title,url,img_url,side_dish,stats,category_id):
        self.cai_menu_service.add_dish(title,url,img_url,side_dish,stats,category_id)