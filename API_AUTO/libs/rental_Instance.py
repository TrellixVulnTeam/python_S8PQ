#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/3/10 11:24
# @Author : ZhangTy
# @File : rental_Instance.py
from pprint import pprint
import random

import requests

from Auth.AutoDL_auth import change_ticket
from common.Request import RequestsHandler
from config.adss import server_ip


# 获取机器列表
def get_instance_list():
    base_url = server_ip()
    url = base_url + 'user/machine/list'
    token = change_ticket()
    header = {
        "Authorization": token
    }
    payload = {"page_index": 1, "page_size": 10, "pay_price_order": "", "region_sign": "nanjing-B"}
    res = RequestsHandler().post_Req(url=url, json=payload, headers=header)
    # pprint(res.json())
    # pprint(res.json()["data"]["list"])
    return res.json()["data"]["list"]


# 获取有空闲GPU的机器
def get_gpu_idle_num():
    for i in get_instance_list():
        # pprint(i)
        mid = []
        if i["gpu_idle_num"] > 1:
            # pprint(i["machine_id"])
            mid.append(i["machine_id"])
            # print(type(mid))
            return random.choice(mid)


# 获取GPU不足的机器
def get_gpu_not_enough():
    for i in get_instance_list():
        # pprint(i)
        mid2 = []
        if i["gpu_idle_num"] < 1:
            # pprint(i["machine_id"])
            mid2.append(i["machine_id"])
            return random.choice(mid2)


if __name__ == '__main__':
    # get_instance_list()
    # get_gpu_idle_num()
    get_gpu_not_enough()
