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
from libs.new_login import Login


class InstanceCreatePayg(BaseApi):

    def creat_instance(self, data):
        resp = self.request_send(data)
        return resp


if __name__ == '__main__':
    ticket = Login().login({"phone": "18801053303", "password": "123456aa", "picture_id": "", "v_code": ""})
    token = Login().get_token({"ticket": ticket}, token=True)
    print(token)
    res = InstanceCreatePayg(token).creat_instance({
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
