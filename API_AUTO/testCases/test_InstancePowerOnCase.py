#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/3/14 16:56
# @Author : ZhangTy
# @File : test_InstancePowerOnCase.py
import os
import sys

from common.Assert import BaseAssert
import allure

from common.Logs import Log
from libs.instance_power_on import InstancePowerOn
import pytest
from utils.handle_yaml import get_yamlCase_data, get_InstancePowerOn_yaml_data
from utils.handle_path import data_path


@allure.epic('AutoDL')
@allure.feature('实例模块')
class TestInstancePowerOn(BaseAssert):

    @pytest.mark.parametrize('title,inBody,expData',
                             get_InstancePowerOn_yaml_data(data_path + 'InstancePowerOnCase.yaml'))
    @allure.story('实例开机接口')
    @allure.title("{title}")
    def test_instance_power_on(self, title, inBody, expData):
        resData = InstancePowerOn().instance_power_on(inData=inBody)
        self.define_assert(resData, expData)
