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


class InstancePay:

    def instance_pay(self, inData):
        base_url = config.adss.server_ip()
        url = base_url + 'order/pay'
        token = get_token()
        header = {'Authorization': token}
        payload = inData
        res = requests.put(url, json=payload, headers=header)
        print(res.json())
        return res.json()


if __name__ == '__main__':
    InstancePay().instance_pay({"order_uuid": ''})
