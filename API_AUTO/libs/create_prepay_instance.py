#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 18:41
# @Author : ZhangTy
# @File : create_prepay_instance.py
from pprint import pprint

import config.adss
from Auth.AutoDL_auth import get_token
from common.BaseApi import BaseApi
from common.Request import RequestsHandler


class InstanceCreatePrepay:

    def creat_instance(self, inData):
        """
        https://test.autodl.com:33443/api/v1/order/pay 预付费订单支付 还没有添加 要添加上
        :param inData:
        :return:
        """
        base_url = config.adss.server_ip()
        url = base_url + 'order/instance/create/prepay'
        token = get_token()
        header = {'Authorization': token}
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        print(res.json())
        return res.json()

    def creat_instance(self, inData):
        base_url = config.adss.server_ip()
        url = base_url + 'order/pay'
        token = get_token()
        header = {'Authorization': token}
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        print(res.json())
        return res.json()

if __name__ == '__main__':
    res = InstanceCreatePrepay().creat_instance({
        "instance_info": {
            "charge_type": "daily",
            "image": "hub.kce.ksyun.com/autodl-image/torch:cuda11.0-cudnn8-devel-ubuntu18.04-py38-torch1.7.0",
            "machine_id": "f94411a60c",
            "instance_name": "",
            "req_gpu_amount": 1,
        },
        "price_info": {
            "charge_type": "daily",
            "duration": 1,
            "machine_id": "f94411a60c",
            "num": 1,
        }
    })
    # pprint(res)
