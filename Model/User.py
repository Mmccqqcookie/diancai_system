#/usr/bin/env python
#-*- coding:utf-8 -*-
from Repository.Userrepository import UserRepository

class model_user:
    def __init__(self,id,email,password,login_time,jiachangcai,xiafancai,sucai,dayudarou,
                 tanggeng,liangcai,suiji_caidan):
        self.id = id
        self.email = email
        self.password = password
        self.login_time = login_time
        self.jiachangcai = jiachangcai
        self.xiafancai = xiafancai
        self.sucai = sucai
        self.dayudarou = dayudarou
        self.tanggeng = tanggeng
        self.liangcai = liangcai
        self.suiji_caidan = suiji_caidan



class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def check_email(self,email):
        result = self.repository.check_email(email)
        return result

    def check_eamil_password(self,email,password):
        result = self.repository.check_email_password(email,password)
        return result

    def update_last_login(self,email,current_time):
        self.repository.update_last_login(email,current_time)


    def update_password(self,email,password):
        self.repository.update_passwrod(email,password)


    def add_email_password(self,email,password):
        self.repository.add_email_password(email,password)

