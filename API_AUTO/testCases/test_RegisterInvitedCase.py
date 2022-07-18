#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/6 10:47
# @Author : ZhangTy
# @File : test_RegisterInvitedCase.py
import allure
import pytest

from common.Assert import BaseAssert
from libs.register_invited import Register
from utils.handle_data import get_phone
from utils.handle_path import data_path
from utils.handle_yaml import get_registerInvited_yaml_data


@allure.epic('AutoDL')
@allure.feature('注册模块')
class TestRegister(BaseAssert):

    @pytest.mark.parametrize('title,inBody,expData',
                             get_registerInvited_yaml_data(data_path + 'RegisterInvitedCase.yaml'))
    @allure.story('邀请注册接口')
    @allure.title("{title}")
    def test_register(self, title, inBody, expData):
        resData = Register().registerInvited(inData=inBody)
        self.define_assert(resData, expData)

    # def get_voucher(self):
    #     phone = get_phone()

if __name__ == '__main__':
    pytest.main('-vs', 'test_RegisterInvitedCase.py')
