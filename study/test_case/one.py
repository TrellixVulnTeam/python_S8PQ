import pytest
from string import Template


# tpe = Template("name is $name, age $age")
# d = {'name': 'zty', 'age': 'age'}
# print(tpe.substitute(d))
# 函数的调用
# def aa():
#     num1 = 10
#     num2 = 20
#     restl = num1 + num2
#     print('%s + %s = %s' % (num1, num2, restl))
#
#
# aa()
#
#
# # 形参
# def bb(a):
#     print('vv', a)
#
#
# # 实参
# bb('1')

# 函数的四种形参
def get(name, age):
    print(name, age)


get('asd', 11)
get(11, 'fasd')
get(name='zty', age=11)


def mypwo(x, y=2):
    print(x * y)


mypwo(4)
mypwo(2, 3)


def mysum(*a):
    sum = 0
    for item in a:
        sum += item
    print(sum)


mysum(1, 2, 3, 4, 5)


def stu(name, age, **kwargs):
    print(name, age)
    print(kwargs)


stu('zty', 18, aa=['asd', '123'], bb=['zgdsd', 'lfask'], eat='12321dsa')

a = 1
print('a=', id(a))
list = [{"name": "推荐食谱", "1": "症状", "name1": "浑身忽冷忽热"}, {"name": "绿豆薏米饭"}, {"name": "芝麻"}]

res = [item[key] for item in list for key in item]
print(res)
for item in list:
    for k, v in item.items():
        print(k, v)
