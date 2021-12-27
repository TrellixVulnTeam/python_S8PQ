#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/15 11:50
# @Author : ZhangTy
# @File : test_InstanceCase.py
import pytest

import config.adss
from Auth.AutoDL_auth import change_ticket
from common.Read_Yaml import get_instance_yaml_data, get_instance_yaml_data2
from common.Request import RequestsHandler
from config.creat_instance import InstanceCreat


class TestInstance:
    # 调用业务代码
    @pytest.mark.parametrize('inBody,expData', get_instance_yaml_data())
    def test_instance(self, inBody, expData):
        resData = InstanceCreat().creat_instance(inData=inBody)
        print("inBody:", inBody)
        print("expData:", expData)
        assert resData['msg'] == expData['msg']
        print(resData['data'])
        return resData['data']


if __name__ == '__main__':
    pytest.main('-vs', 'test_RechargeCase.py')
