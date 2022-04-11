#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/3/14 15:30
# @Author : ZhangTy
# @File : instance_power_on.py
import config
from config.adss import server_ip
from Auth.AutoDL_auth import get_token
import requests
from common.Request import RequestsHandler


class InstancePowerOn:
    def instance_power_on(self, inData):
        base_url = config.adss.server_ip()
        url = base_url + 'instance/power_on'
        token = get_token()
        header = {"Authorization": token}
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        return res.json()


if __name__ == '__main__':
    InstancePowerOn().instance_power_on({"instance_uuid": "f94411a60c-df3185ed", "payload": ""})
