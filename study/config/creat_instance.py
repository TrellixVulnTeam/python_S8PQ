#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/15 14:39
# @Author : ZhangTy
# @File : creat_instance.py
import config.adss
from Auth.AutoDL_auth import change_ticket
from common.Request import RequestsHandler


class InstanceCreat:

    def creat_instance(self, inData):
        base_url = config.adss.server_ip()
        url = base_url + 'order/instance/create/payg'
        token = change_ticket()
        header = {'Authorization': token}
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        return res.json()


if __name__ == '__main__':
    res = InstanceCreat().creat_instance({
        "instance_info": {
            "charge_type": "payg",
            "image": "hub.kce.ksyun.com/autodl-image/torch:cuda11.0-cudnn8-devel-ubuntu18.04-py38-torch1.7.0",
            "machine_id": "c1ef11a4ac",
            "instance_name": "",
            "req_gpu_amount": 1,
        },
        "price_info": {
            "charge_type": "payg",
            "duration": 1,
            "machine_id": "c1ef11a4ac",
            "num": 1,
        }
    })
    print(res)
