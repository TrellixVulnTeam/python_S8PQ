#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/28 11:34
# @Author : ZhangTy
# @File : instance_release.py
# 3-释放实例
import time
from common.BaseApi import BaseApi
import config
from Auth.AutoDL_auth import get_token
from common.Request import RequestsHandler
from config.adss import server_ip
from libs.instance_list import InstanceList


class InstanceRelease(BaseApi):

    def instance_release(self):
        base_url = config.adss.server_ip()
        url = base_url + 'instance/release'
        token = get_token()
        header = {'Authorization': token}
        uuid_list = InstanceList().get_shutdown_InstanceList()
        print(uuid_list)

        for uid in uuid_list:
            print(uid)
            payload = {
                "instance_uuid": uid
            }
            res = RequestsHandler().post_Req(url, json=payload, headers=header)
            time.sleep(1)
            print(res.json())


if __name__ == '__main__':
    InstanceRelease().instance_release()
