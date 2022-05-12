#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/25 15:21
# @Author : ZhangTy
# @File : 创建100个文件夹.py
import os

# path = 'C:\\Users\\张铁瀛\\Desktop\\123'
# for i in range(100):
#     dirName = path + '\\' + 'a' + str(i + 1)
#     print(dirName)
#     os.makedirs(path + '\\' + dirName)
#     with open(dirName, 'w+', encoding='utf-8') as file1:
#         file1.write('test')
#
# path = 'C:\\Users\\张铁瀛\\Desktop\\'
# # 定义文件夹名称
# name = "zty"
# # 创建10个文件夹，序号为0-9
# for i in range(10):
#     # "文件"+
#     # os.path.exists(path) 判断文件是否存在 固定语法，记住就行
#     # 定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字
#     # name+str(i+1)为拼接 名称，效果为：Python剑雅1，Python剑雅2...
#     # str(i+1)提高用户体验1，2，3，...
#     isExists = os.path.exists(path + name + str(i + 1))
#
#     if not isExists:
#
#         # os.path.exists(path+str(i)) 创建文件夹 路径+名称
#         os.makedirs(path + name + str(i + 1))
#         print("%s 目录创建成功" % i)
#     else:
#         print("%s 目录创建成功" % i)
#
#         # 如果文件不存在,则继续上述操作,直到循环结束
#         continue
import os


def create_dir(des, name, n):
    os.chdir(des)
    os.mkdir(name)
    # 创建了新目录，如果要在里面创建文件，就需要更改地址
    os.chdir(des + '/' + name)
    # print(os.getcwd())
    file_ex = input('输入要创建的文件名称样例: ')
    # 从右往左分割
    file_ex = file_ex.rpartition('.')
    # print(file_ex)
    for i in range(n):
        file = open(file_ex[0] + str(i) + file_ex[1] + file_ex[2], 'w')
        file.close()


# 这里是要创建新目录的地址
des = 'C:\\Users\\张铁瀛\\Desktop\\123'
name = input('输入要创建的文件名：')
n = int(input('要创建的文件个数：'))
create_dir(des, name, n)


