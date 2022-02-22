#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/2/17 17:17
# @Author : ZhangTy
# @File : 面向对象.py
"""
类+实例的例子

"""


class zheng:  # 类
    def __init__(self, length, width):  # 初始化方法  下面的函数直接调用就可以 公用的
        self.length = length
        self.width = width

    def mianji(self):
        return self.width * self.length


if __name__ == '__main__':
    rec = zheng(1, 3)  # 类的实例
    print(rec.__dict__)  # 实例的属性
    print(rec.mianji())
    print(hasattr(str, 'replace'))  # 在对象里面找有没有某个属性或方法，返回值是布尔型
    print(hasattr(zheng, 'length'))  # 类没有length 因为类本身还没有生成实例
    print(hasattr(rec, 'length'))  # 实例会有length
    print(getattr(zheng, 'length', '没有找到'))  # 找不到属性或方法，返回指定的值
    print(getattr(rec, 'length', 'abc'))  # 在对象里面找有没有某个属性，返回是方法本身
    print(setattr(rec, 'length', 2))
