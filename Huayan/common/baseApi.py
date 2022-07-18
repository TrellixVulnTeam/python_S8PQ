#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/7 16:39
# @Author : ZhangTy
# @File : baseApi.py
"""
    1- 为所有的业务模块提供的基本接口操作，增删改查+发送
    2- 日志  截图都可以在积累里面封装
    3- 断言方法

封装思路：

"""
import requests
from utils.hand_yaml import get_yaml_data
import inspect
from configs.adss import server_ip


class BaseAPI:
    # 初始化方法
    # self.__class__.__name__ 根据类名去获取
    def __init__(self):
        self.data = get_yaml_data('../configs/apiPathConfig.yaml')[self.__class__.__name__]
        print('类名是------->', self.__class__.__name__)
        print('类数据是------->', self.data)

    # 公共发送方法，每一个接口都会调用  , params=None, files=None, id=''
    def request_send(self, json=None, params=None, files=None, id=''):
        # requests.request(method, url)
        api_data = self.data[inspect.stack()[1][3]]
        print(api_data)
        print(server_ip() + api_data["path"])
        print(api_data['method'])
        print(json)
        resp = requests.request(
            method=api_data['method'],
            url=f'{server_ip()}{api_data["path"]}',
            json=json,
            params=params,
            files=files
        )
        # print(resp.json())
        return resp.json()
