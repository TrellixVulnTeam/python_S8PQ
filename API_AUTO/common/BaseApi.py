#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/7 10:38
# @Author : ZhangTy
# @File : BaseApi.py
import inspect

import requests
from utils.handle_yaml import get_yaml_data
from config.adss import server_ip


class BaseApi:
    def __init__(self, token=None):
        if token:
            self.header = {'Authorization': token}
        else:
            self.header = None
        # 获取对应模块的接口信息
        self.data = get_yaml_data('../data/apiPathConfig.yaml')[self.__class__.__name__]  # 根据类名获取

    def request_send(self, json=None, params=None, files=None, id=''):
        try:
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
                files=files,
                id=id,
                headers=self.header
            )
            return resp.json()
        except:
            pass
