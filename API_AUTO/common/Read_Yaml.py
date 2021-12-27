from string import Template

import yaml
from config_path import get_login_yaml_path, get_register_yaml_path, get_recharge_yaml_path, get_instance_yaml_path
from common import Random_number


def get_login_yaml_data():
    reqList = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    # 1- 读取文件操作，从磁盘读取到内存
    fo = open(get_login_yaml_path(), 'r', encoding="utf-8")
    # 2- 使用yaml方法获取数据
    res1 = yaml.load(fo, Loader=yaml.FullLoader)
    print(res1)
    fo.close()
    # 删掉下标0的无用数据 删除集合里面的{'url': 'login', 'method': 'POST'}字典
    del res1[0]
    for one1 in res1:
        reqList.append((one1['data'], one1['resp']))

    # print('>> reqList: ', reqList)
    # print('>> reqList len: ', reqList.__len__())

    return reqList  # 存放结果[(请求1,响应1),(请求2,期望响应2)]


def get_register_yaml_data():
    res3 = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    # 1- 读取文件操作，从磁盘读取到内存
    fo = open(get_register_yaml_path(), 'r', encoding="utf-8")
    # 2- 使用yaml方法获取数据
    res1 = yaml.load(fo, Loader=yaml.FullLoader)
    print('del res1[0]: ', res1[0])
    del res1[0]

    # yml 文件数据，转 python 类型
    num = Random_number.main()
    tempTemplate1 = Template(str(res1))
    c = tempTemplate1.safe_substitute({"phone": num})
    res2 = yaml.safe_load(c)
    # print('>> yaml_data: ', res2)
    # print('>> yaml_data len: ', res2.__len__())

    # print(type(tempTemplate1))

    for one1 in res2:
        res3.append((one1['data'], one1['resp']))

    print('>> reqList: ', res3)
    print('>> reqList len: ', res3.__len__())

    return res3


def get_recharge_yaml_data():
    reqList = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    # 1- 读取文件操作，从磁盘读取到内存
    fo = open(get_recharge_yaml_path(), 'r', encoding="utf-8")
    # 2- 使用yaml方法获取数据
    res1 = yaml.load(fo, Loader=yaml.FullLoader)
    print(res1)
    fo.close()
    # 删掉下标0的无用数据 删除集合里面的{'url': 'login', 'method': 'POST'}字典
    del res1[0]
    for one1 in res1:
        reqList.append((one1['data'], one1['resp']))

    # print('>> reqList: ', reqList)
    # print('>> reqList len: ', reqList.__len__())

    return reqList  # 存放结果[(请求1,响应1),(请求2,期望响应2)]


def get_instance_yaml_data():
    reqList = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    # 1- 读取文件操作，从磁盘读取到内存
    fo = open(get_instance_yaml_path(), 'r', encoding="utf-8")
    # 2- 使用yaml方法获取数据
    res1 = yaml.load(fo, Loader=yaml.FullLoader)
    print(res1)
    fo.close()
    # 删掉下标0的无用数据 删除集合里面的{'url': 'login', 'method': 'POST'}字典
    del res1[0]

    for one1 in res1:
        # v = {'data': one1['data'], 'resp': one1['resp']}
        reqList.append((one1['data'], one1['resp']))

    print('>> reqList: ', reqList)
    print('>> reqList len: ', reqList.__len__())

    return reqList  # 存放结果[(请求1,响应1),(请求2,期望响应2)]


def get_instance_yaml_data2():
    reqList = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    # 1- 读取文件操作，从磁盘读取到内存
    fo = open(get_instance_yaml_path(), 'r', encoding="utf-8")
    # 2- 使用yaml方法获取数据
    res1 = yaml.load(fo, Loader=yaml.FullLoader)
    print(res1)
    fo.close()
    # 删掉下标0的无用数据 删除集合里面的{'url': 'login', 'method': 'POST'}字典
    del res1[0]

    """
    old tuple
     (
    [0]-'data'
    [1]-'resp'
    )...
    
    new tuple
    (
    [0]-{'data','resp'}
    [1]-{'data','resp'}
    ...
    )
    """

    for one1 in res1:
        v = {'data': one1['data'], 'resp': one1['resp']}
        reqList.append(v)

    print('>> reqList: ', reqList)
    print('>> reqList len: ', reqList.__len__())

    return reqList  # 存放结果[(请求1,响应1),(请求2,期望响应2)]


if __name__ == '__main__':
    get_register_yaml_data()
    get_instance_yaml_data()
    # req = get_login_yaml_data()
    # for one in req:
    #     print(one)
