#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/24 11:30
# @Author : ZhangTy
# @File : instance_list.py
import time

import config.adss
from Auth.AutoDL_auth import change_ticket
from common.Request import RequestsHandler


class InstanceList:

    def get_running_InstanceList(self):
        base_url = config.adss.server_ip()
        url = base_url + 'instance'
        token = change_ticket()
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
        print(fs)
        return fs

    def is_all_shutdown_InstanceList(self, uuidList):
        base_url = config.adss.server_ip()
        url = base_url + 'instance'
        token = change_ticket()
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
        token = change_ticket()
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
        print(fs)
        return fs


if __name__ == '__main__':
    InstanceList().get_running_InstanceList()
