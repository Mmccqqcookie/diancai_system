#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Author : hucheng-self
    @Time : 2018/8/4 16:35
"""
from IRepository.ICaiMenuRepository import IcaimenuRepository
from DB.model import *
from DB.settings import DBconon
import Model.CaiMenu


class CaiMenuRepository(IcaimenuRepository):
    def __init__(self):
        self.db_coon = DBconon()
        self.Session = sessionmaker(bind=DBconon().engine())
        self.session = self.Session()

    def check_dish_exits(self, title):
        result = self.session.query(Caidan).filter_by(title=title).first()
        if result:
            model_cai_menu = Model.CaiMenu.Model_caiMenu(id=result.id, title=result.title, url=result.url,
                                                         img_url=result.img_url,
                                                         side_dish=result.side_dish, stats=result.stats,
                                                         category_id=result.category_id)
            return model_cai_menu
        else:
            return None

    def add_dish(self, title, url, img_url, side_dish, stats, category_id):
        self.session.add(
            Caidan(title=title, url=url, img_url=img_url, side_dish=side_dish, stats=stats, category_id=category_id))
        self.session.commit()
