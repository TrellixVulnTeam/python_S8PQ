#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/1/13 15:28
# @Author : ZhangTy
# @File : conftest.py
import pytest

from libs.instance_list import InstanceList
from libs.login import Login

"""
autouse = True: 一般是整个项目里需要自检操作

autouse = False: 默认是False，需要手动调用，哪里需要调到哪里去
"""


# @pytest.fixture(scope='session', autouse=True)
# def start_running():
#     print('>>>AutoDL自动化测试开始执行')
#     yield
#     print('>>>AutoDL自动化测试结束执行')

#
# # 登录操作,其他的业务层测试代码需要调用这个登录
# @pytest.fixture(scope='function')
# def login_init():
#     print('>>>用户操作登录')
#     token = Login().login({"phone": "18801053303", "password": "123456Aa", "picture_id": "", "v_code": ""},
#                           getToken=True)
#     yield token  # 返回token值
#     print('---登录初始化操作完成---')

#
# @pytest.fixture(scope='module')
# def instance_release():
#     print(">>>>>>>>>>>正在执行释放实例接口")
#     yield
#     print(TestInstance().test_instance_release())
#     print(">>>>>>>>>>>实例全部释放完成")

#
# def test01(instance_release):
#     print(">>>开始清理")
