#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/7 17:14
# @Author : ZhangTy
# @File : hand_yaml.py
import yaml


def get_yaml_data(file_path: str):
    with open(file_path, encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())


if __name__ == '__main__':
    res = get_yaml_data('../configs/apiPathConfig.yaml')
    print(res)
