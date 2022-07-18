#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/6 17:55
# @Author : ZhangTy
# @File : conftest.py

import pytest


@pytest.fixture(scope='session', autouse=False)
def fix_test_01():
    print('\n001 setup')
    yield
    print('\n001 teardown')


