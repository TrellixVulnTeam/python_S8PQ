#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/3/8 11:43
# @Author : ZhangTy
# @File : 访问百度并搜索.py
from selenium import webdriver

# 创建浏览器驱动对象，打开空白的浏览器
driver = webdriver.Chrome()

# 访问所在的网址
driver.get('https://test.autodl.com:33443/login')
