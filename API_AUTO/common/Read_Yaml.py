from pprint import pprint
from string import Template

import yaml
from config_path import get_login_yaml_path, get_register_yaml_path
from Auth.AutoDL_auth import get_captcha
from data import Random_number


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
        cap_id, cap_val = get_captcha()
        one1['data']['captcha_id'] = cap_id
        one1['data']['captcha_value'] = cap_val
        reqList.append((one1['data'], one1['resp']))

    return reqList  # 存放结果[(请求1,响应1),(请求2,期望响应2)]


def get_register_yaml_data():
    reqList = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    # 1- 读取文件操作，从磁盘读取到内存
    fo = open(get_register_yaml_path(), 'r', encoding="utf-8")
    # 2- 使用yaml方法获取数据
    res1 = yaml.load(fo, Loader=yaml.FullLoader)
    del res1[0]
    num = Random_number.main()
    tempTemplate1 = Template(str(res1))
    # print(type(tempTemplate1))
    c = tempTemplate1.safe_substitute({"phone": num})
    for one1 in res1:
        reqList.append((one1['data'], one1['resp']))

    # yml 文件数据，转 python 类型
    yaml_data = yaml.safe_load(c)
    print(yaml_data)
    return yaml_data


if __name__ == '__main__':
    get_register_yaml_data()
    # req = get_login_yaml_data()
    # for one in req:
    #     print(one)
