#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/14 11:36
# @Author : ZhangTy
# @File : test_RechargeCase.py
import pytest

from common.Read_Yaml import get_recharge_yaml_data
from config.recharge import Recharge


class TestRecharge:
    # 调用业务代码
    @pytest.mark.parametrize('inBody,expData', get_recharge_yaml_data())
    def test_register(self, inBody, expData):
        resData = Recharge().wx_recharge(inData=inBody)
        assert resData['msg'] == expData['msg']


if __name__ == '__main__':
    pytest.main('-vs', 'test_RechargeCase.py')
