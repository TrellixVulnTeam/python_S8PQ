#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/2/15 15:41
# @Author : ZhangTy
# @File : 爬虫.py
import json

import requests
import re

from pymysql.constants.FIELD_TYPE import JSON

"""
1.提取章节名
2.提取网址名
3.提取正文
4.写入文件

re.S 允许跨行匹配
"""

url = 'http://www.quannovel.com/read/620/'
req = requests.post(url)
# print(req.text)
title_list = re.findall('class="name ">(.*?)</a>', req.text, re.S)  # re.S 允许跨行匹配
url_list = re.findall('href="(.*?).html"', req.text)

dict1 = {}
for i in range(len(title_list)):
    dict1[title_list[i]] = f'{url}{url_list[i]}.html'

for k, v in dict1.items():
    # print(k, v)
    req = requests.post(v)
    # print(req.text)
    text_list = re.findall('class="page-content ">(.*?)class="reward"', req.text, re.S)
    for j in k:  # 标题
        for i in text_list:  # 文章
            filepath = f'./data/{k}.txt'
            file1 = open(filepath, 'w')
            file1.write(i.replace('<p>', '').replace('</p>', ''))
            file1.close()
