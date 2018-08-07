#/usr/bin/env python
#-*- coding:utf-8 -*-
from Model.User import UserService
from Service.user.response import Response
from Service.user.ModelView import User_Model_View


class User_Service:
    def __init__(self):
        self.response = Response()
        self.userService = UserService()
        self.model = None

    def check_email(self,email):
        result = self.userService.check_email(email)
        try:
            if result:
                raise Exception('邮箱已注册！！！')
        except Exception as e:
            self.response.status = False
            self.response.message = str(e)
        return self.response

    def check_email_password(self,email,password):
        self.model = self.userService.check_eamil_password(email,password)
        try:
            if self.model:
                model_view = User_Model_View(id=self.model.id,email=self.model.password,password=self.model.password,
                                             login_time=self.model.login_time,suiji_caidan=self.model.suiji_caidan)
                self.response.model_view = model_view
            else:
                raise Exception('邮箱密码不匹配')
        except Exception as e:
            self.response.status = False
            self.response.message = str(e)

        return self.response


    def update_password(self,email,password):
        try:
            self.userService.update_password(email,password)

        except Exception as e:
            self.response.status = False
            self.response.message = '更新密码出错，稍后修改'
        return self.response


    def update_last_login(self,email):
        import datetime
        current_time = datetime.datetime.now()
        try:
            self.userService.update_last_login(email,current_time)

        except Exception as e:
            self.response.status = False
            self.response.message = '数据库错误，更新登入时间失败'

        return self.response


    def add_email_password(self,email,password):
        try:
            self.userService.add_email_password(email,password)
        except Exception as e:
            self.response.status = False
            self.response.message = str(e)
        return self.response

