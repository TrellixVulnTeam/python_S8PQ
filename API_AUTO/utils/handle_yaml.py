#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/1/12 11:39
# @Author : ZhangTy
# @File : handle_yaml.py
from string import Template

import yaml

from common import Random_number


def get_yamlCase_data(fileDir):
    reslist = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    with open(fileDir, encoding='utf-8') as fo:
        res = yaml.safe_load(fo.read())
        # print(res)
        for one in res:
            reslist.append((one['detail'], one['data'], one['resp']))
            # print(reslist)
        return reslist


# 注册用例
def get_register_yaml_data(fileDir):
    res3 = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    with open(fileDir, encoding='utf-8') as fo:
        res = yaml.safe_load(fo.read())
    # yml 文件数据，转 python 类型
    num = Random_number.main()
    tempTemplate1 = Template(str(res))
    c = tempTemplate1.safe_substitute({"phone": num})
    res2 = yaml.safe_load(c)
    # print('>> yaml_data: ', res2)
    # print('>> yaml_data len: ', res2.__len__())

    # print(type(tempTemplate1))

    for one1 in res2:
        res3.append((one1['detail'], one1['data'], one1['resp']))
    return res3


if __name__ == '__main__':
    print(get_yamlCase_data('../data/LoginCase.yaml'))
    print(get_register_yaml_data('../data/RegisterCase.yaml'))
