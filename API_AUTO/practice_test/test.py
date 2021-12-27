# !C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/17 11:10
# @Author : ZhangTy
# @File : test.py
import time

import config.adss
from cases.test_InstanceCase import *


def creat_instance():
    base_url = config.adss.server_ip()
    url = base_url + 'order/instance/create/payg'
    token = change_ticket()
    header = {'Authorization': token}
    payload = {
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
    }
    res = RequestsHandler().post_Req(url, json=payload, headers=header)
    print(res.json())
    return res.json()


def test_instance_poweroff():
    base_url = config.adss.server_ip()
    url = base_url + 'instance/power_off'
    token = change_ticket()
    header = {'Authorization': token}

    tt = TestInstance()

    inBody = get_instance_yaml_data2()
    for oneTest in inBody:
        uuid = tt.test_instance_unit(oneTest['data'], oneTest['resp'])
        print("instance_uuid:", uuid)
        payload = {
            "instance_uuid": uuid
        }

        # TODO: for -> starting / 3s

        time.sleep(5)

        print("will stop this instance: ", payload)
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        print(res)

    return str(res)



if __name__ == '__main__':
    test_instance_poweroff()
