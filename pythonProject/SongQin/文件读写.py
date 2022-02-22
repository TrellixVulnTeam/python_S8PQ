#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/1/5 16:18
# @Author : ZhangTy
# @File : 文件读写.py
"""
w+ 可以同时读写，如果文件不存在，则新建文件，写入时清空输入
r+ 可以同时读写，如果文件不存在，则报错，写入时是追加写入
a+ 可以同时读写，如果文件不存在，则新建文件，写入时是追加写入

使用seek时，要注意中文是两个字节
file.seek(2)光标回到文件收尾，里面的数字控制回到稳健首位之后，偏移多少位
如果第二个参数为1，表示保持光标当前位置，如果第二个参数为2，表示光标移动到文件末尾，第二个参数是1,2时，只有wb模式可以使用


# 快速生成1000个账号 账号为zty001,123456
with open(filepath2, 'w+', encoding='utf-8') as f:
    for i in range(1,1001):
        f.write(f'zty{i:03},123456\n')
"""

# filepath = 'test.txt'
# file1 = open(filepath, 'w')
# file1.write('abc')
# file1.close()
# # 读取文件
# filepath = 'test.txt'
# file1 = open(filepath)
# print(file1.read())
# file1.close()


# filepath = '1.txt'
# file1 = open(filepath, 'a+')
# file1.write('mnb')
# file1.seek(0)
# print(file1.readlines())
# file1.close()


# file2 = open(filepath2, encoding='utf-8')
# # print(file2.read())         # 读取文件所有内容，返回的是字符串
# # print(file2.readline())   # 读取文件第一行内容
# # print(file2.readlines())  # 读取文件所有内容，返回的是列表 读取一行可以使用下标读取
# print(file2.read().splitlines())  # 读取文件所有内容，返回是列表，不出现\n
# file2.close()


# 快速生成1000个账号 账号为zty001,123456
# with open(filepath2, 'w+', encoding='utf-8') as f:
#     for i in range(1,1001):
#         f.write(f'zty{i:03},123456\n')
# with open('d:/春夜喜雨.txt','w+') as file1:
#     file1.write('好雨知时节,当春乃发生')
#     file1.seek(2,1)
#     f1=file1.read()
#     print(f1)

# dict10={'ABC':'ABCDE','YOU':'YOURS','HIJKL':'MN'}
# print(dict10.clear())

# {i:05}i 不足5位的时候，补齐5位
# with open('D:/账号220116.txt', 'w+') as file1:
#     for i in range(1, 1000):
#         file1.write(f'sq{i:05},{i:05}\n')

filepath2 = 'zhanghao2.txt'
with open(filepath2, 'a+') as file1:
    for i in range(1, 10):
        file1.write(f'zty+{i:05},123456aa\n')

# 读取多个文件
# with open() as a, open()
