#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/11 14:19
# @Author : ZhangTy
# @File : new_login.py
from common.BaseApi import BaseApi
from utils.handle_data import get_sha1


class Login(BaseApi):
    def login(self, data):
        data['password'] = get_sha1(data['password'])
        resp = self.request_send(data)
        # if getToken:
        #     return resp['data']['token']
        return resp['data']['ticket']

    def get_token(self, data, token=False):
        resp = self.request_send(data)
        if token:
            return resp['data']['token']
        return resp


if __name__ == '__main__':
    res = Login().login({"phone": "18801053303", "password": "123456aa", "picture_id": "", "v_code": ""})

    ticket = Login().login({"phone": "18801053303", "password": "123456aa", "picture_id": "", "v_code": ""})
    res1 = Login().get_token({"ticket": ticket})
    print(res1)
