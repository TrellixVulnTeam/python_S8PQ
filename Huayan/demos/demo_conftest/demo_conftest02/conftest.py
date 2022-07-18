#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/6 18:00
# @Author : ZhangTy
# @File : conftest.py
import pytest


@pytest.fixture(scope='session', autouse=False)
def fix_test_02():
    print('\n002 setup')
    yield
    print('\n002 teardown')

@pytest.fixture(scope='session', autouse=False)
def fix_test_03(fix_test_01):
    print('\n003 setup')
    yield
    print('\n003 teardown')