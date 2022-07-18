#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/3/31 17:26
# @Author : ZhangTy
# @File : handle_data.py
import hashlib

# from utils.handle_yaml import get_registerInvited_yaml_data
import random
import string


def get_sha1(pwd):
    # 实例化对象
    md5 = hashlib.sha1()
    # 调用加密方法直接加密
    md5.update(pwd.encode("utf-8"))
    # 返回md5加密的结果
    return md5.hexdigest()  # 转成 16进制值


# 运营商的号码前缀
prefix = [
    '130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
    '145', '147', '149', '150', '151', '152', '153', '155', '156', '157',
    '158', '159', '165', '171', '172', '173', '174', '175', '176', '177',
    '178', '180', '181', '182', '183', '184', '185', '186', '187', '188',
    '189', '191'
]


def builder():
    # 随机取一个手机号前缀
    pos = random.randint(0, len(prefix) - 1)
    # 随机生成后8位数字，string.digits是数字0到9，可以参考源码
    suffix = ''.join(random.sample(string.digits, 8))
    # 拼接返回11位手机号
    return prefix[pos] + suffix


def main():
    # 生成5个手机号码
    for i in range(0):
        print(builder())
    return builder()


if __name__ == '__main__':
    get_sha1()
