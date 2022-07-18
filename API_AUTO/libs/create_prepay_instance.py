#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/11 18:41
# @Author : ZhangTy
# @File : create_prepay_instance.py
from pprint import pprint
import requests
import config.adss
from Auth.AutoDL_auth import get_token
from common.BaseApi import BaseApi
from common.Request import RequestsHandler
from libs.Instance_info import get_gpu_idle_num
from libs.new_login import Login


class InstanceCreatePrepay(BaseApi):

    def creat_instance_prepay(self, data):
        resp = self.request_send(data)
        return resp


if __name__ == '__main__':
    # 登录
    ticket = Login().login({"phone": "18801053303", "password": "123456aa", "picture_id": "", "v_code": ""})
    # 用ticket换token
    token = Login().get_token({"ticket": ticket}, token=True)
    res = InstanceCreatePrepay(token).creat_instance_prepay({
        "instance_info": {
            "charge_type": "daily",
            "image": "hub.kce.ksyun.com/autodl-image/torch:cuda11.0-cudnn8-devel-ubuntu18.04-py38-torch1.7.0",
            "machine_id": get_gpu_idle_num(),
            "instance_name": "",
            "req_gpu_amount": 1,
        },
        "price_info": {
            "charge_type": "daily",
            "duration": 1,
            "machine_id": get_gpu_idle_num(),
            "num": 1,
        }
    })
    print(res)
    # pprint(res)
