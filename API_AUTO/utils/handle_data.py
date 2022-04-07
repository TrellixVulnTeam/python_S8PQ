#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/3/31 17:26
# @Author : ZhangTy
# @File : handle_data.py
import hashlib


def get_sha1(pwd):
    # 实例化对象
    md5 = hashlib.sha1()
    # 调用加密方法直接加密
    md5.update(pwd.encode("utf-8"))
    # 返回md5加密的结果
    return md5.hexdigest()  # 转成 16进制值
