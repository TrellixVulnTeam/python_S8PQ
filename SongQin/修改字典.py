#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/5/12 16:47
# @Author : ZhangTy
# @File : 修改字典.py

D = {'one': 1, 'two': 2}

D.update({'three': 3, 'four': 4}) # 传一个字典
print(D)

D.update(five=5, six=6) # 传关键字
print(D)

D.update([('seven', 7), ('eight', 8)]) # 传一个包含一个或多个元祖的列表
print(D)

D.update(zip(['eleven', 'twelve'], [11, 12])) # 传一个zip()函数
print(D)

D.update(one=111, two=222) # 使用以上任意方法修改存在的键对应的值
print(D)