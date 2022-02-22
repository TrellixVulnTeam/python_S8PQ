#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/2/14 15:11
# @Author : ZhangTy
# @File : 冒泡排序.py

# 自动补齐自定义的段落


# 列表排序

# list1 = [1, 3, 42, 41, 52, 2, 36, -5]
# new = sorted(list1, reverse=True)
# print(new)

# 冒泡算法
list1 = [1, 3, 42, 41, 52, 2, 36, -5]
for i in range(len(list1) - 1):
    for j in range(len(list1) - 1 - i):
        if list1[j] > list1[j + 1]:
            print(f'第{j}位和第{j+1}位的顺序不对')
            print(f'变化之前是>>>>>>>>>>>>>>>{list1}')
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
            print(f'变化之前后>>>>>>>>>>>>>>>{list1}')
    print(f'第{i+1}轮比较结束')
print(list1)
