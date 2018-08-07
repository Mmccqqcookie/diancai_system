#/usr/bin/env python
#-*- coding:utf-8 -*-
from IRepository.ICaileibieRepository import IcaicategoryRepository
from DB.model import *
from DB.settings import DBconon
import Model.CaiCategory

class caiCategoryRepository(IcaicategoryRepository):
    def __init__(self):
        self.db_coon = DBconon()
        self.Session = sessionmaker(bind=DBconon().engine())
        self.session = self.Session()


    def check_category_exist(self,category_url):
        result = self.session.query(Caidan).filter_by(category_url=category_url).first()
        if result:
            model_cai_category = Model.CaiCategory.model_caicategory(id=result.id,category=result.category,category_url=result.category_url)
            return model_cai_category
        else:
            return None

    def update_category(self,category,category_url):
        self.session.query(Caidan).filter_by(category=category).update({'category_url':category_url})
        self.session.commit()


    def add_category(self,category,category_url):
        self.session.add(User(category=category,category_url=category_url))
        self.session.commit()


