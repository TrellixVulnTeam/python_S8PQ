#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/6 10:30
# @Author : ZhangTy
# @File : register_invited.py
from pprint import pprint

import config.adss
from common.BaseApi import BaseApi
from common import Random_number
from common.Request import RequestsHandler
from libs.new_login import Login


class Register(BaseApi):

    def registerInvited(self, data):
        resp = self.request_send(data)
        return resp


if __name__ == '__main__':
    # 登录
    ticket = Login().login({"phone": "18801053303", "password": "123456aa", "picture_id": "", "v_code": ""})
    # 用ticket换token
    token = Login().get_token({"ticket": ticket}, token=True)
    num = Random_number.main()
    res = Register(token).registerInvited(
        {"invite_code": "487686b5-637f-4d99-8202-7c0b29fa322d", "phone_area": "+86", "password": "123456Aa",
         "phone": num, "v_code": "666666"})
    pprint(res)
