#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/1/13 15:28
# @Author : ZhangTy
# @File : conftest.py
import pytest

from libs.instance_list import InstanceList
from libs.login import Login
from libs.creat_instance import InstanceCreat

"""
autouse = True: 一般是整个项目里需要自检操作

autouse = False: 默认是False，需要手动调用，哪里需要调到哪里去

scope='session' 整个自动化运行，只做一次
    1.环境检查
    2.登录
model和class的区别，model模块级别是一个文件下有多个类，class级别只有一个类

有返回值：如果一个fixture需要使用另一个fixture返回值，直接使用它的函数名
没有返回值：@pytest.mark.usefixtures

"""


@pytest.fixture(scope='session', autouse=True)
def start_running():
    print('>>>AutoDL自动化测试开始执行')


# 1.登录
@pytest.fixture(scope='session')
def login_init():
    print('>>>开始执行登录')
    token = Login().login({"phone": "18801053303", "password": "123456Aa", "picture_id": "", "v_code": ""},
                          getToken=True)
    yield token
    print('>>>登录初始化操作完成')


# 2.创建实例
@pytest.fixture(scope='session')
def instance_init(login_init):
    print('>>>创建实例')
    instance_obj = InstanceCreat().creat_instance(login_init)

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
