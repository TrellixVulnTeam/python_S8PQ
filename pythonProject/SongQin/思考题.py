#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/1/21 16:13
# @Author : ZhangTy
# @File : 思考题.py
# import copy
#
# list1 = [100, 200, 300, [700, 800, 900]]
# list1_new = list1  # 赋值,没有生成新的对象
# list1_new2 = copy.copy(list1)  # 浅拷贝,生成了新的对象,如果列表中有子列表,子列表仍然是同一个对象
# list1_new1 = copy.deepcopy(list1)  # 深拷贝,列表和子列表都是新对象
#
# print(list1_new2)

# 写一个号段筛选程序,需求如下:
# 用户从控制台输入一个手机号，判断出运营商(移动（假设号段是130-150）、
# 联通（假设是151-170）、电信（假设是171-199）),如果用户输入的位数不对，提示用户位数有误;如果用户输入非数字，提示有非法字符

# input1 = input('请输入您的手机号：')
# if not input1.isdigit():
#     print('您输入的不是数字')
# else:
#     if len(input1) != 11:
#         print('您输入的位数不对')
#     else:
#         num1 = int(input1[0:3])
#         if 130 <= num1 <= 150:
#             print('移动')
import random

print(random.choice(['烤肉', '披萨']))
