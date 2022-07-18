#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/12 18:32
# @Author : ZhangTy
# @File : instance_pay.py
import config.adss
from Auth.AutoDL_auth import get_token
from common.BaseApi import BaseApi
from common.Request import RequestsHandler
import requests
from common.BaseApi import BaseApi
from libs.new_login import Login


class InstancePay(BaseApi):

    def instance_pay(self, data):
        resp = self.request_send(data)
        return resp


if __name__ == '__main__':
    # 登录
    ticket = Login().login({"phone": "18801053303", "password": "123456aa", "picture_id": "", "v_code": ""})
    # 用ticket换token
    token = Login().get_token({"ticket": ticket}, token=True)
    res = InstancePay(token).instance_pay({"order_uuid": '319683944793316821'})
    print(res)
