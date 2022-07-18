#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/1/13 15:28
# @Author : ZhangTy
# @File : conftest.py
import pytest

import config.adss
from Auth.AutoDL_auth import get_token
from common.Request import RequestsHandler
from libs.create_payg_instance import InstanceCreatePayg
from libs.create_prepay_instance import InstanceCreatePrepay
from libs.Instance_info import get_gpu_idle_num, get_instance_gpu_num
from libs.instance_list import InstanceList
from libs.instance_release import instance_release
from libs.login import Login

"""
autouse = True: 一般是整个项目里需要自检操作

autouse = False: 默认是False，需要手动调用，哪里需要调到哪里去

scope='session' 整个自动化运行，只做一次
    1.环境检查
    2.登录
model和class的区别，model模块级别是一个文件下有多个类，class级别只有一个类

有返回值：如果一个fixture需要使用另一个fixture返回值，直接使用它的函数名
没有返回值：@pytest.mark.usefixtures

"""


# 释放实例
@pytest.fixture(scope='session', autouse=True)
def start_running():
    print('>>>AutoDL自动化测试开始执行')
    yield
    # instance_release()
    print('>>>AutoDL自动化测试执行结束，清除数据')
    if InstanceList().get_shutdown_InstanceList3() == 30:
        print('>>>>>>实例列表超过30个实例，即将释放全部实例')
        instance_release()
        print(">>>>>>实例已经全部释放")


# 1.登录
@pytest.fixture(scope='session')
def login_init():
    print('>>>开始执行登录')
    token = Login().login({"phone": "18801053303", "password": "123456Aa", "picture_id": "", "v_code": ""},
                          getToken=True)
    yield token
    print('>>>登录初始化操作完成')


# 2.创建预付费订单
@pytest.fixture(scope='function')
def create_prepay_order():
    print('>>>正在创建包年包月订单')
    order = InstanceCreatePrepay().creat_instance_prepay({
        "instance_info": {
            "charge_type": "daily",
            "image": "hub.kce.ksyun.com/autodl-image/torch:cuda11.0-cudnn8-devel-ubuntu18.04-py38-torch1.7.0",
            "machine_id": get_gpu_idle_num(),
            "instance_name": "",
            "req_gpu_amount": 1,
        },
        "price_info": {
            "charge_type": "daily",
            "duration": 1,
            "machine_id": get_gpu_idle_num(),
            "num": 1,
        }
    })
    # print(order['data']['runtime_info']['order_uuid'])
    yield order['data']['runtime_info']['order_uuid']
    print('>>>已经创建包年包月订单')


# 3.创建按量计费，租用全部剩余GPU，让机器没有剩余GPU，部分case需要GPU不足的情况
@pytest.fixture(scope='function')
def rent_all():
    print('>>>>>>开始创建实例')
    InstanceCreatePayg().creat_instance({
        "instance_info": {
            "charge_type": "payg",
            "image": "hub.kce.ksyun.com/autodl-image/torch:cuda11.0-cudnn8-devel-ubuntu18.04-py38-torch1.7.0",
            "machine_id": get_gpu_idle_num(),
            "instance_name": "",
            "req_gpu_amount": get_instance_gpu_num(),
        },
        "price_info": {
            "charge_type": "payg",
            "duration": 1,
            "machine_id": get_gpu_idle_num(),
            "num": get_instance_gpu_num(),
        }
    })
    yield
    base_url = config.adss.server_ip()
    url = base_url + 'instance/power_off'
    token = get_token()
    header = {'Authorization': token}
    uuid_list = InstanceList().get_running_InstanceList()
    print(uuid_list)

    for uid in uuid_list:
        print(uid)
        payload = {
            "instance_uuid": uid
        }
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        print(res.json())
    print(">>>>>>实例已经关机")


# 4、关机所有实例，目的为了腾出GPU便于其他用例使用，否则会导致GPU不足部分用例执行失败
@pytest.fixture(scope='function')
def powerOff_all():
    print('>>>>>>开始执行')
    yield
    print('>>>>>>结束运行')

# 4.
# # 2.创建实例
# @pytest.fixture(scope='session')
# def instance_init(login_init):
#     print('>>>创建实例')
#     instance_obj = InstanceCreat().creat_instance(login_init)

# @pytest.fixture(scope='session', autouse=True)
# def start_running():
#     print('>>>AutoDL自动化测试开始执行')
#     yield
#     print('>>>AutoDL自动化测试结束执行')
#
# # 登录操作,其他的业务层测试代码需要调用这个登录
# @pytest.fixture(scope='function')
# def login_init():
#     print('>>>用户操作登录')
#     token = Login().login({"phone": "18801053303", "password": "123456Aa", "picture_id": "", "v_code": ""},
#                           getToken=True)
#     yield token  # 返回token值
#     print('---登录初始化操作完成---')

#
# @pytest.fixture(scope='module')
# def instance_release():
#     print(">>>>>>>>>>>正在执行释放实例接口")
#     yield
#     print(TestInstance().test_instance_release())
#     print(">>>>>>>>>>>实例全部释放完成")

#
# def test01(instance_release):
#     print(">>>开始清理")
