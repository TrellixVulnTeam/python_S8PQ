#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/12 18:07
# @Author : ZhangTy
# @File : test_InstancePrepayCase.py
import os
import sys

import allure
import pytest

import config.adss
from Auth.AutoDL_auth import get_token
from common.Assert import BaseAssert
from common.Logs import Log
from common.Request import RequestsHandler
from libs.create_payg_instance import InstanceCreatePayg
from libs.create_prepay_instance import InstanceCreatePrepay
from libs.instance_list import InstanceList
from utils.handle_path import data_path
from utils.handle_yaml import get_CreatePrepayInstance_yaml_data


@allure.epic('AutoDL')
@allure.feature('实例模块')
class TestCreatePrepayInstance(BaseAssert):

    @pytest.mark.parametrize('title,inBody,expData',
                             get_CreatePrepayInstance_yaml_data(data_path + 'InstanceCreatePrepayCase.yaml'))
    @allure.story('创建包年包月实例订单接口')
    @allure.title("{title}")
    def test_instance(self, title, inBody, expData):
        resData = InstanceCreatePrepay().creat_instance_prepay(inData=inBody)
        print(resData)
        self.define_assert(resData, expData)

