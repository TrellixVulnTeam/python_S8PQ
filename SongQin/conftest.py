#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/5/17 18:03
# @Author : ZhangTy
# @File : conftest.py

import pytest


@pytest.fixture(scope='function')
def aa():
    print('开始')
    yield
    print('结束')
