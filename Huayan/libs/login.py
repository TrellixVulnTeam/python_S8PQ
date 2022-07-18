#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/7 17:24
# @Author : ZhangTy
# @File : login.py
from common.baseApi import BaseAPI
from utils.handle_data import get_sha1


class Login(BaseAPI):

    def login(self, data):
        data['password'] = get_sha1(data['password'])
        resp = self.request_send(data)
        # print(resp)
        return resp


if __name__ == '__main__':
    res = Login().login({"phone": "18801053333", "password": "123456Aa", "picture_id": "", "v_code": ""})
    print(res)
