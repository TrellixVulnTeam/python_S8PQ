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


class InstanceCreatePrepay:

    def creat_instance_prepay(self, inData):
        base_url = config.adss.server_ip()
        url = base_url + 'order/instance/create/prepay'
        token = get_token()
        header = {'Authorization': token}
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        print(res.json())
        return res.json()


if __name__ == '__main__':
    res = InstanceCreatePrepay().creat_instance_prepay({
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
    print(res['data']['runtime_info']['order_uuid'])
    # pprint(res)
