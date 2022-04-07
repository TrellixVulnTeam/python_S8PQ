#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/7 10:38
# @Author : ZhangTy
# @File : BaseApi.py
class BaseApi:
    def __init__(self, token=None):
        if token:
            self.header = {'Authorization': token}
        else:
            self.header = None
