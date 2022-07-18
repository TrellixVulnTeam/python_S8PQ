#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/6 17:59
# @Author : ZhangTy
# @File : test_02.py
import pytest


def test_02(fix_test_01,fix_test_02):
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-sv',__file__])
