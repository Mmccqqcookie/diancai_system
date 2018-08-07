#/usr/bin/env python
#-*- coding:utf-8 -*-
import tornado.web
from Common.Session import seesion as Csession
from Common.send_email import Send_email
from Common.random_str import Random_str
from Service.user.ServiceUser import User_Service


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.SendEmail = Send_email()
        self.Randomstr = Random_str()
        self.userservice = User_Service()

    def get_current_user(self):
        csession = Csession(self)
        if self.get_cookie('__ranstr__'):
            if csession['__login']:
                login = csession['__login']
                return login
            else:
                return False
        else:
            return False


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index/index.html',login_user = self.current_user)


class LoginHandler(BaseHandler):
    def post(self, *args, **kwargs):
        cession = Csession(self)
        email = self.get_argument('email')
        password = self.get_argument('password')
        reponse = self.userservice.check_email_password(email,password)
        if reponse.status:
            cession['__login'] = self.get_argument('email')
            data = {'status':reponse.status}

        else:
            data = {'status':reponse.status,'message':reponse.message}

        self.write(data)

class LogoutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        cession = Csession(self)
        del cession['del']
        if not cession['__login']:
            self.redirect('/')

class SearchKeywordHandler(BaseHandler):
    def get(self, *args, **kwargs):
        from Common.sousuocaimin import get_search_html
        keyword = self.get_argument('keyword')
        data,url = get_search_html(keyword)
        data = {'status':True,'data':data,'category':url}
        self.write(data)


class PageTabHandler(BaseHandler):
    def get(self, *args, **kwargs):
        from Common.sousuocaimin import page_tab_data
        page = self.get_argument('page',None)
        if page:
            url = 'http://xiachufang.com' + self.request.path +'?page=' + str(page)
        else:
            url = 'http://xiachufang.com' + self.request.path
        print(url)
        data = page_tab_data(url,self.request.path)
        data = {'status': True, 'data': data}
        self.write(data)


class Send_EmailHandler(BaseHandler):
    def post(self, *args, **kwargs):
        print(self.request.path)
        email = self.get_argument('email')
        response = self.userservice.check_email(email)
        if response.status:
            random_str = self.Randomstr.random_str()
            status = self.SendEmail.Send_to_email(email,random_str)
            if status:
                data = {'status':status,'message':'已发送','code':random_str}
            else:
                data = {'status':status,'message':'邮箱错误'}
        else:
            data = {'status':response.status,'message':response.message}

        self.write(data)


class ResgistrHandler(BaseHandler):
    def post(self, *args, **kwargs):
        email = self.get_argument('email')
        password = self.get_argument('password')
        response = self.userservice.add_email_password(email,password)
        if response.status:
            pass
        else:
            data = {'status':response.status,'message':response.message}
            self.write(data)


class AddDishMenuHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('index/add_caidan.html',login_user=self.current_user)





