#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/5/17 18:10
# @Author : ZhangTy
# @File : 测试conftest.py
import allure
import pytest

from common.Assert import BaseAssert
from libs.login import Login
from utils.handle_path import data_path
from utils.handle_yaml import get_yamlCase_data

#
# @allure.epic('AutoDL')
# @allure.feature('登录模块')
# class TestLogin(BaseAssert):
#     # 调用业务代码
#
#     @pytest.mark.parametrize('title,inBody,expData', get_yamlCase_data(data_path + 'LoginCase.yaml'))  # 数据驱动方法
#     @allure.story('登录接口')
#     @allure.title("{title}")  # 用例标题
#     def test_login(self, title, inBody, expData, rent_all):
#         # 1- 调用业务层封装的接口代码
#         resData = Login().login(inData=inBody)
#         self.define_assert(resData, expData)
#
#
# if __name__ == '__main__':
#     pytest.main(['-vs', '-w', '测试conftest.py'])
