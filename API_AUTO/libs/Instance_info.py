#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/3/10 11:24
# @Author : ZhangTy
# @File : Instance_info.py
from pprint import pprint
import random

import requests

from Auth.AutoDL_auth import get_token
from common.Request import RequestsHandler
from config.adss import server_ip


# 获取机器列表
def get_instance_list():
    base_url = server_ip()
    url = base_url + 'user/machine/list'
    token = get_token()
    header = {
        "Authorization": token
    }
    payload = {"page_index": 1, "page_size": 10, "pay_price_order": "", "region_sign": "nanjing-B"}
    res = RequestsHandler().post_Req(url=url, json=payload, headers=header)
    # pprint(res.json())
    # pprint(res.json()["data"]["list"])
    return res.json()["data"]["list"]


# 获取订单列表
def get_order_list():
    base_url = server_ip()
    url = base_url + 'order/list'
    token = get_token()
    header = {
        "Authorization": token
    }
    payload = {"page_index": 1, "page_size": 10, "pay_price_order": "", "region_sign": "nanjing-B"}
    res = RequestsHandler().post_Req(url=url, json=payload, headers=header)
    # pprint(res.json())
    # pprint(res.json()["data"]["list"])
    return res.json()["data"]["list"]


# 获取机器剩余GPU
def get_instance_gpu_num():
    list1 = get_instance_list()
    # pprint(list1)
    # print(type(list1))
    list2 = get_gpu_idle_num()
    # print(type(list2))
    for i in list1:
        # print(i)
        if list2 in i.values():
            # print(i["gpu_idle_num"])
            # gpu_num = list1[0]["gpu_idle_num"]
            # print(gpu_num)
            # print('找到gpu空闲机器的ID了')
            return i["gpu_idle_num"]


# 获取有空闲GPU的机器
def get_gpu_idle_num():
    for i in get_instance_list():
        # pprint(i)
        mid = []
        if i["gpu_idle_num"] > 0:
            # pprint(i["machine_id"])
            mid.append(i["machine_id"])
            # print(type(mid))
            # print(mid)
            return i["machine_id"]


# 获取GPU不足的机器
def get_gpu_not_enough():
    for i in get_instance_list():
        mid2 = []
        if i["gpu_idle_num"] == 0:
            # pprint(i["machine_id"])
            mid2.append(i["machine_id"])
            # print(i["machine_id"])
            return i["machine_id"]


# 获取待支付的订单
def get_unpaid_order():
    for i in get_order_list():
        if i["status"] == "unpaid":
            # print(i['uuid'])
            return i["uuid"]


if __name__ == '__main__':
    get_instance_gpu_num()
    # get_gpu_idle_num()
    # get_instance_gpu_num()
