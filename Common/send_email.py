#/usr/bin/env python
#-*- coding:utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

class Send_email():
    def __init__(self):
        #qq邮箱smtp服务器
        self.host_server = 'smtp.qq.com'
        #sender_qq为发件人的qq号码
        self.sender_qq = 'XXXXX'
        #pwd为qq邮箱的授权码
        self.pwd = 'XXXXXX'
        #发件人的邮箱
        self.sender_qq_mail = 'XXXXX@qq.com'
        #收件人邮箱
        self.receiver = None
        #邮件的正文内容
        self.mail_content = '''
        您好 !
            现在正在注册《随机点菜系统》您的随机验证码是%s
            请您在5分钟之类完成注册!'''
        #邮件标题
        self.mail_title = '**随机点菜系统** 注册 验证码'

    def Send_to_email(self,send_to_mail,random_str):
        #ssl登录
        self.receiver = send_to_mail
        self.mail_content = self.mail_content %random_str
        smtp = SMTP_SSL(self.host_server)
        #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(0)
        smtp.ehlo(self.host_server)
        smtp.login(self.sender_qq, self.pwd)

        msg = MIMEText(self.mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(self.mail_title, 'utf-8')
        msg["From"] = self.sender_qq_mail
        msg["To"] = self.receiver
        try:
            smtp.sendmail(self.sender_qq_mail, self.receiver, msg.as_string())
            return True
        except Exception as e:
            return False
        smtp.quit()

