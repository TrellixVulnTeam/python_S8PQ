#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/15 11:50
# @Author : ZhangTy
# @File : test_InstancePaygCase.py
import os
import sys
import time

import allure
import pytest

import config.adss
from Auth.AutoDL_auth import get_token
from common.Assert import BaseAssert
from common.Logs import Log
from common.Request import RequestsHandler
from libs.create_payg_instance import InstanceCreatePayg
from libs.instance_list import InstanceList
from utils.handle_path import data_path
from utils.handle_yaml import get_CreatePaygInstance_yaml_data


@allure.epic('AutoDL')
@allure.feature('实例模块')
class TestCreatePaygInstance(BaseAssert):
    # 1-创建实例
    """
     每次执行的时候需要把一个机器剩余的卡全部租用完，否则有一条用例会失败
    """
    # @pytest.mark.skipif(reason='没有空闲GPU，不执行该用例')
    @pytest.mark.parametrize('title,inBody,expData',
                             get_CreatePaygInstance_yaml_data(data_path + 'InstanceCreatePaygCase.yaml'))
    @allure.story('创建按量计费实例接口')
    @allure.title("{title}")
    def test_payg_instance(self, title, inBody, expData):
        resData = InstanceCreatePayg().creat_instance(inData=inBody)
        self.define_assert(resData, expData)

    # 2-实例关机
    @pytest.mark.last
    @allure.story('实例关机接口')  # 接口名称
    @allure.title('实例关机用例')  # 用例标题
    def test_instance_poweroff(self):
        base_url = config.adss.server_ip()
        url = base_url + 'instance/power_off'
        token = get_token()
        header = {'Authorization': token}
        uuid_list = InstanceList().get_running_InstanceList()
        print(uuid_list)

        for uid in uuid_list:
            print(uid)
            payload = {
                "instance_uuid": uid
            }
            res = RequestsHandler().post_Req(url, json=payload, headers=header)
            print(res.json())

        # 500ms * 10 = 5s, timeout=5s
        all_shutdown = False

        for i in range(10):
            all_shutdown = InstanceList().is_all_shutdown_InstanceList(uuid_list)
            if all_shutdown:
                break
            print("waiting...")
            time.sleep(1)

        if all_shutdown:
            print("succeed")
        else:
            print("failed")


if __name__ == '__main__':
    pytest.main('-vs', 'test_InstancePaygCase.py')
