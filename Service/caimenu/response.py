#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Author : hucheng-self
    @Time : 2018/8/4 17:08
"""

class Response:
    def __init__(self,status=True,message='',model_view=None):
        self.status = status
        self.message = message
        self.model_view = model_view

