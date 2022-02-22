#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/1/5 15:46
# @Author : ZhangTy
# @File : 循环.py

# for i in range(1, 10, 2):
#     print(i)

# 打印100以内的偶数
# i = 2
# while i <= 100:
#     print(i)
#     i += 2

# i = 2
# for i in range(1, 100, 2):
#     i += 1
#     print(i)


# break终止循环 continue 跳出档次循环
# for i in range(1, 11):
#     if i == 6:
#         # break
#         continue
#     print(i)

# 倒计时程序
import time

#
# for i in range(10, 0, -1):
#     print(f'\r倒计时{i}秒', end='')  # \r光标回到行首 #end=''每次不需要换行
#     time.sleep(1)
# else:
#     print('\r倒计时结束')
#
# for i in range(1, 11):
#     print(i)

# i = 2
# while i <= 100:
#     print(i)
#     i += 2
# print( 'my name is %s'.format('Mike'))

for i in range(100, 10, -10):
    print(f'\r倒计时{i}秒', end='')
    time.sleep(1)
else:
    print('\r倒计时结束')
