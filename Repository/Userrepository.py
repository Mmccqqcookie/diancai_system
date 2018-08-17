#/usr/bin/env python
#-*- coding:utf-8 -*-

from IRepository.IUserrepository import IUserrepository
from DB.model import *
from DB.settings import DBconon
import Model.User

class UserRepository(IUserrepository):
    def __init__(self):
        self.db_coon = DBconon()
        self.Session = sessionmaker(bind=DBconon().engine())
        self.session = self.Session()

    def fetch_one_message(self,email):
        result = self.session.query(User).filter_by(email=email).first()
        if result:
            modeluser = Model.User.model_user(id=result.id, email=result.email, password=result.password,
                                              login_time=result.last_login, jiachangcai=result.jiachangcai,
                                              xiafancai=result.xiafancai, sucai=result.sucai,
                                              dayudarou=result.dayudarou,
                                              tanggeng=result.tanggeng, liangcai=result.liangcai,
                                              suiji_caidan=result.suiji_candan)
            return modeluser
        else:
            return False


    def check_email(self,email):
        result = self.session.query(User).filter_by(email=email).first()
        if result:
            return True
        else:
            return False

    def check_email_password(self,email,password):
        result = self.session.query(User).filter(and_(User.email==email,User.password==password)).first()
        if result:
            modeluser = Model.User.model_user(id=result.id, email=result.email, password=result.password,
                                              login_time=result.last_login,jiachangcai=result.jiachangcai,
                                              xiafancai=result.xiafancai,sucai=result.sucai,dayudarou=result.dayudarou,
                                              tanggeng=result.tanggeng,liangcai=result.liangcai, suiji_caidan=result.suiji_candan)
            return modeluser
        else:
            return False

    def update_last_login(self,email,current_time):
        self.session.query(User).filter_by(email=email).update({'last_login':current_time})
        self.session.commit()

    def update_passwrod(self,email,password):
        self.session.query(User).filter_by(email=email).update({'password':password})
        self.session.commit()

    def update_dish(self,user,jiachangcai=None,xiafancai=None,sucai=None,dayudarou=None,
                    tanggeng=None,liangcai=None):
        if jiachangcai:
            self.session.query(User).filter_by(email=user).update({'jiachangcai':jiachangcai})
        if xiafancai:
            self.session.query(User).filter_by(email=user).update({'xiafancai':xiafancai})
        if sucai:
            self.session.query(User).filter_by(email=user).update({'sucai':sucai})
        if dayudarou:
            self.session.query(User).filter_by(email=user).update({'dayudarou':dayudarou})
        if tanggeng:
            self.session.query(User).filter_by(email=user).update({'tanggeng':tanggeng})
        if liangcai:
            self.session.query(User).filter_by(email=user).update({'liangcai':liangcai})

        self.session.commit()

    def add_email_password(self,email,password):
        self.session.add(User(email=email,password=password))
        self.session.commit()
