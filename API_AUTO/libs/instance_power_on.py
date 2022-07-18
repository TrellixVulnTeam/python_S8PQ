#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/3/14 15:30
# @Author : ZhangTy
# @File : instance_power_on.py
import config
from config.adss import server_ip
from Auth.AutoDL_auth import get_token
from common.BaseApi import BaseApi
import requests
from common.Request import RequestsHandler
from libs.new_login import Login


class InstancePowerOn(BaseApi):
    def instance_power_on(self, data):
        resp = self.request_send(data)
        return resp


if __name__ == '__main__':
    # 登录
    ticket = Login().login({"phone": "18801053303", "password": "123456aa", "picture_id": "", "v_code": ""})
    # 用ticket换token
    token = Login().get_token({"ticket": ticket}, token=True)
    res = InstancePowerOn(token).instance_power_on({"instance_uuid": "f94411a60c-ad0d9501", "payload": ""})
    print(res)
