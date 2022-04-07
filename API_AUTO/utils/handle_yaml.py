#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/1/12 11:39
# @Author : ZhangTy
# @File : handle_yaml.py
import json
from pprint import pprint
import random

from libs.instance_list import InstanceList
import yaml
from common import Random_number
from libs.rental_Instance import get_gpu_idle_num, get_gpu_not_enough, get_instance_gpu_num
from jinja2 import Template
import utils.ReadYamlRender
from utils.ReadYamlRender import ReadYamlRender


def get_yamlCase_data(fileDir):
    reslist = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    with open(fileDir, encoding='utf-8') as fo:
        res = yaml.safe_load(fo.read())
        # print(res)
        for one in res:
            reslist.append((one['detail'], one['data'], one['resp']))
            # print(reslist)
        return reslist


# 获取注册yaml用例
def get_register_yaml_data(fileDir):
    res3 = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    with open(fileDir, encoding='utf-8') as fo:
        res = yaml.safe_load(fo.read())
    # yml 文件数据，转 python 类型
    num = Random_number.main()
    new_data = {"phone": num}
    res1 = Template(str(res)).render(new_data)
    results = yaml.safe_load(res1)
    # a = ReadYamlRender('../data/RegisterCase.yaml', {"phone": num}).render
    for one1 in results:
        res3.append((one1['detail'], one1['data'], one1['resp']))
    return res3


# 获取创建实例yaml用例
def get_CreatInstance_yaml_data(fileDir):
    reslist = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    with open(fileDir, encoding='utf-8') as fo:
        res = yaml.safe_load(fo.read())
    mid1 = get_gpu_idle_num()
    mid2 = get_gpu_not_enough()
    num = get_instance_gpu_num()
    new_data = {"machine_id": [mid1, mid2]}  # 多参数写成字典 字典里可以加列表
    res1 = Template(str(res)).render(new_data)
    # print(res1)
    results = yaml.safe_load(res1)
    for one in results:
        reslist.append((one['detail'], one['data'], one['resp']))
    return reslist


# 获取实例开机yaml用例
def get_InstancePowerOn_yaml_data(fileDir):
    reslist = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    with open(fileDir, encoding='utf-8') as fo:
        res = yaml.safe_load(fo.read())
    mid1 = InstanceList().found_gpu_EnoughInstance()
    # mid1 = random.choice(uuidlist)
    mid2 = InstanceList().found_gpu_NotEnoughInstance()
    new_data = {'instance_uuid': [mid1, mid2]}  # 列表类型数据   使用下标获取，例如：{{instance_uuid.0}}
    res1 = Template(str(res)).render(new_data)
    results = yaml.safe_load(res1)
    for one in results:
        reslist.append((one['detail'], one['data'], one['resp']))
    # print(reslist)
    return reslist


if __name__ == '__main__':
    pprint(get_CreatInstance_yaml_data('../data/InstanceCreateCase.yaml'))
    # pprint(get_register_yaml_data('../data/RegisterCase.yaml'))
    # pprint(get_InstancePowerOn_yaml_data('../data/InstancePowerOnCase.yaml'))
