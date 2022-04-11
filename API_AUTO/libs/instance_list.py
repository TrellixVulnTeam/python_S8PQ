#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/24 11:30
# @Author : ZhangTy
# @File : instance_list.py
import time
from pprint import pprint

import config.adss
from Auth.AutoDL_auth import get_token
from common.Request import RequestsHandler
from libs.rental_Instance import get_gpu_not_enough, get_gpu_idle_num


class InstanceList:

    def get_running_InstanceList(self):
        base_url = config.adss.server_ip()
        url = base_url + 'instance'
        token = get_token()
        header = {'Authorization': token}
        payload = {
            "date_from": "",
            "date_to": "",
            "page_index": 1,
            "page_size": 20
        }
        res = RequestsHandler().get_Req(url, params=payload, headers=header)
        # pprint(res.json())
        resp = res.json()
        fs = []
        for i in resp['data']["list"]:
            if i["status"] == "running" or i["status"] == "starting":
                # print(i["uuid"])
                fs.append(i["uuid"])
        # print(fs)
        return fs

    def is_all_shutdown_InstanceList(self, uuidList):
        base_url = config.adss.server_ip()
        url = base_url + 'instance'
        token = get_token()
        header = {'Authorization': token}
        payload = {
            "date_from": "",
            "date_to": "",
            "page_index": 1,
            "page_size": 20
        }
        res = RequestsHandler().get_Req(url, params=payload, headers=header)
        # pprint(res.json())
        resp = res.json()

        all_shutdown = True
        for i in resp['data']["list"]:
            if i["uuid"] in uuidList and i["status"] != "shutdown":
                all_shutdown = False
                return all_shutdown

        return all_shutdown

    def get_shutdown_InstanceList(self):
        base_url = config.adss.server_ip()
        url = base_url + 'instance'
        token = get_token()
        header = {'Authorization': token}
        payload = {
            "date_from": "",
            "date_to": "",
            "page_index": 1,
            "page_size": 1000
        }
        res = RequestsHandler().get_Req(url, params=payload, headers=header)
        # pprint(res.json())
        resp = res.json()
        fs = []
        for i in resp['data']["list"]:
            if i["status"] == "shutdown":
                # print(i["uuid"])
                fs.append(i["uuid"])
        # print(fs)
        return fs

    def get_shutdown_InstanceList2(self):
        base_url = config.adss.server_ip()
        url = base_url + 'instance'
        token = get_token()
        header = {'Authorization': token}
        payload = {
            "date_from": "",
            "date_to": "",
            "page_index": 1,
            "page_size": 1000
        }
        res = RequestsHandler().get_Req(url, params=payload, headers=header)
        resp = res.json()
        list1 = []
        for i in resp['data']["list"]:
            if i["status"] == "shutdown":
                list1.append(i)
        # pprint(list1)
        return list1

    def found_gpu_NotEnoughInstance(self):
        machine_list = get_gpu_not_enough()  # 获取没有GPU的机器ID
        for i in self.get_shutdown_InstanceList2():
            # print(i)
            if machine_list == i['machine_id']:  # 没有GPU的机器ID与我的实例列表已经关机的实例的机器ID匹配
                # print('机器ID和获取实例里面的机器ID对上了')
                # print(i['uuid'])
                return i['uuid']

    def found_gpu_EnoughInstance(self):
        machine_list = get_gpu_idle_num()  # 获取有GPU的机器ID
        for i in self.get_shutdown_InstanceList2():
            # print(i)
            if machine_list == i['machine_id']:  # 没有GPU的机器ID与我的实例列表已经关机的实例的机器ID匹配
                # print('机器ID和获取实例里面的机器ID对上了')
                # print(i['uuid'])
                return i['uuid']


if __name__ == '__main__':
    InstanceList().found_gpu_EnoughInstance()
    # InstanceList().get_shutdown_InstanceList2()
    # InstanceList().get_shutdown_InstanceList()
