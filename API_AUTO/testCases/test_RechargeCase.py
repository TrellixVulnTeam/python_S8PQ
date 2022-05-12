#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/14 11:36
# @Author : ZhangTy
# @File : test_RechargeCase.py
import os
import sys

import allure
import pytest

from common.Assert import BaseAssert
from common.Logs import Log
from libs.recharge import Recharge
from utils.handle_path import data_path
from utils.handle_yaml import get_yamlCase_data

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger


@allure.epic('AutoDL')
@allure.feature('充值模块')
class TestRecharge(BaseAssert):
    # 调用业务代码

    @pytest.mark.parametrize('title,inBody,expData', get_yamlCase_data(data_path + '\\WxRechargeCase.yaml'))
    @allure.story('微信充值接口')
    @allure.title("{title}")
    def test_wx_register(self, title, inBody, expData):
        resData = Recharge().wx_recharge(inData=inBody)
        self.define_assert(resData, expData)

    @allure.story('支付宝充值接口')  # 接口名称
    @pytest.mark.parametrize('title,inBody,expData', get_yamlCase_data(data_path + 'AlipayRechargeCase.yaml'))
    @allure.title("{title}")
    def test_alopay_register(self, title, inBody, expData):
        resData = Recharge().alipay_recharge(inData=inBody)
        self.define_assert(resData, expData)


if __name__ == '__main__':
    pytest.main('-vs', 'test_RechargeCase.py')
