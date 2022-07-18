#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/8 15:51
# @Author : ZhangTy
# @File : register.py
from common.baseApi import BaseAPI
from utils.handle_data import main


class Register(BaseAPI):

    def register(self, data):
        resp = self.request_send(data)
        return resp


if __name__ == '__main__':
    num = main()
    res = Register().register({"phone_area": "+86", "password": "123456Aa", "phone": num, "v_code": "666666"})
    print(res)
