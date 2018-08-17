#/usr/bin/env python
#-*- coding:utf-8 -*-

from Service.user.ServiceUser import User_Service
from Service.caimenu.ServiceCaiMenu import CaiMenu_Service
from Common.sousuocaimin import get_search_html
import random

class SuijiDish:
    def __init__(self,handler,email):
        self.handler = handler
        self.email = email
        self.userservice = User_Service()
        self.caimenuservice = CaiMenu_Service()
        self.data = []
        self.jcc_n = None
        self.xfc_n = None
        self.sc_n = None
        self.yr_n = None
        self.ta_n = None
        self.lc_n = None

    def Get_cate_Num(self):
        self.jcc_n = self.handler.get_argument('jiachangcai',0)
        self.xfc_n = self.handler.get_argument('xiafancai',0)
        self.sc_n = self.handler.get_argument('sucai',0)
        self.yr_n = self.handler.get_argument('dayudarou',0)
        self.tg_n = self.handler.get_argument('tg',0)
        self.lc_n = self.handler.get_argument('liangcai',0)

    def Get_email_mysql_cate_dish(self):
        self.Get_cate_Num()
        email_cate_dish = self.userservice.fetch_oen_message(self.email)
        jiachangcai = email_cate_dish.model_view.jiachangcai.split(' ')

        xiafancai = email_cate_dish.model_view.xiafancai.split(' ')
        sucai = email_cate_dish.model_view.sucai.split(' ')
        dayudarou = email_cate_dish.model_view.dayudarou.split(' ')
        tanggeng = email_cate_dish.model_view.tanggeng.split(' ')
        liangcai = email_cate_dish.model_view.liangcai.split(' ')
        self.check_add_list_data(self.jcc_n,jiachangcai,cate='jiachangcai')
        self.check_add_list_data(self.xfc_n,xiafancai,cate='xiafancai')
        self.check_add_list_data(self.sc_n,sucai,cate='sucai')
        self.check_add_list_data(self.yr_n,dayudarou,cate='dayudarou')
        self.check_add_list_data(self.tg_n,tanggeng,cate='tanggeng')
        self.check_add_list_data(self.lc_n,liangcai,cate='liangcai')

        return self.data

    def check_add_list_data(self,category_num,categorys,cate=None):

        if category_num == "":
            category_num = '0'
        if int(category_num) > len(categorys):
            for dish in categorys:
                print(dish)
                result = self.caimenuservice.check_dish_exits(dish)
                if result.status:
                    dish_detail = {'title':result.model_view.title,
                            'url':result.model_view.url,
                            'img':result.model_view.img_url,
                            'side_dish':result.model_view.side_dish,
                            'stats':result.model_view.stats}
                    self.data.append(dish_detail)
                else:
                    dish_detail = get_search_html(dish,perfect_match=True,cate=cate)
                    self.data.append(dish_detail)

        else:
            suijicaidan = random.sample(categorys,int(category_num))
            print(suijicaidan)
            for dish in suijicaidan:
                result = self.caimenuservice.check_dish_exits(dish)
                if result.status:
                    dish_detail = {'title': result.model_view.title,
                                   'url': result.model_view.url,
                                   'img': result.model_view.img_url,
                                   'side_dish': result.model_view.side_dish,
                                   'stats': result.model_view.stats}
                    self.data.append(dish_detail)
                else:
                    dish_detail = get_search_html(dish, perfect_match=True, cate=cate)
                    self.data.append(dish_detail)


