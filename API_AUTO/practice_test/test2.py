# #!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# # -*- coding: utf-8 -*-
# # @Time : 2021/12/17 11:43
# # @Author : ZhangTy
# # @File : test2.py
# import traceback
# from pprint import pprint
import os
import sys

from common.Logs import Log

file = os.path.basename(sys.argv[0])
print(file)
log = Log(file)
print(log)
logger = log.Logger
