#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/14 11:36
# @Author : ZhangTy
# @File : test_RechargeCase.py
import allure
import pytest

from common.Assert import BaseAssert
from libs.recharge import Recharge
from utils.handle_path import data_path
from utils.handle_yaml import get_yamlCase_data


class TestRecharge(BaseAssert):
    # 调用业务代码
    @allure.story('充值接口')  # 接口名称
    # @allure.title('充值用例')  # 用例标题
    @pytest.mark.parametrize('title,inBody,expData', get_yamlCase_data(data_path + '\\RechargeCase.yaml'))
    @allure.title("{title}")
    def test_register(self, title, inBody, expData):
        resData = Recharge().wx_recharge(inData=inBody)
        print("inBody:", inBody)
        print("expData:", expData)
        print(resData)
        self.define_assert(resData, expData)


if __name__ == '__main__':
    pytest.main('-vs', 'test_RechargeCase.py')
