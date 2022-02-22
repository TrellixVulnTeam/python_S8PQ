#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/1/12 11:39
# @Author : ZhangTy
# @File : handle_path.py
import os

# 当前文件路径
# print(__file__)

# 上一级路径
# print(os.path.dirname(__file__))

# 项目路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试数据路径
data_path = os.path.join(project_path, 'data')

# log 路径
log_path = os.path.join(project_path, 'logs\\log')

# 报告路径
report_path = os.path.join(project_path, 'report\\reportallure')

#
if __name__ == '__main__':
    print('项目路径>>>', project_path)
    print('测试数据路径>>>', data_path)
    print('日志路径>>>', log_path)
    print('报告路径>>>', report_path)
