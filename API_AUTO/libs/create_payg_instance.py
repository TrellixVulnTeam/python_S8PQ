#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/15 14:39
# @Author : ZhangTy
# @File : create_payg_instance.py
from pprint import pprint

import config.adss
from Auth.AutoDL_auth import get_token
from common.BaseApi import BaseApi
from common.Request import RequestsHandler


class InstanceCreatePayg:

    def creat_instance(self, inData):
        base_url = config.adss.server_ip()
        url = base_url + 'order/instance/create/payg'
        token = get_token()
        header = {'Authorization': token}
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        return res.json()


if __name__ == '__main__':
    res = InstanceCreatePayg().creat_instance({
        "instance_info": {
            "charge_type": "payg",
            "image": "hub.kce.ksyun.com/autodl-image/torch:cuda11.0-cudnn8-devel-ubuntu18.04-py38-torch1.7.0",
            "machine_id": "f94411a60c",
            "instance_name": "",
            "req_gpu_amount": 1,
        },
        "price_info": {
            "charge_type": "payg",
            "duration": 1,
            "machine_id": "f94411a60c",
            "num": 1,
        }
    })
    pprint(res)
