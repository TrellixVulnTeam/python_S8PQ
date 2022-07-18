#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/6 17:59
# @Author : ZhangTy
# @File : test_02.py
import pytest

@pytest.mark.skip()
def test_03(fix_test_03):
    assert 1 == 1


def test_04(fix_test_03, fix_test_01):
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-sv', __file__])
