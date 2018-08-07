#/usr/bin/env python
#-*- coding:utf-8 -*-
from Repository.CaicategoryRepository import caiCategoryRepository

class model_caicategory:
    def __init__(self,id,category,category_url):
        self.id = id
        self.category = category
        self.category_url = category_url


class CaiCategoryService:
    def __init__(self):
        self.repository = caiCategoryRepository()

    def check_category_exist(self,category_url):
        result = self.repository.check_category_exist(category_url)
        if result:
            return result
        else:
            return None

    def update_category(self,category,category_url):
        self.repository.update_category(category,category_url)


    def add_category(self,category,category_url):
        self.repository.add_category(category,category_url)

