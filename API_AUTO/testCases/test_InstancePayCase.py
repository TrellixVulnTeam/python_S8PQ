#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/12 19:20
# @Author : ZhangTy
# @File : test_InstancePayCase.py
import allure, pytest
import config.adss
from Auth.AutoDL_auth import get_token
from common.Assert import BaseAssert
from common.Logs import Log
from common.Request import RequestsHandler
from libs.create_payg_instance import InstanceCreatePayg
from libs.instance_list import InstanceList
from libs.instance_pay import InstancePay
from utils.handle_path import data_path
from utils.handle_yaml import get_CreatePaygInstance_yaml_data, get_InstancePay_yaml_data


@allure.epic('AutoDL')
@allure.feature('实例模块')
class TestCreatePagInstance(BaseAssert):
    """
    使用fixture前置条件：创建包年包月订单 create_prepay_order
    """
    @pytest.mark.parametrize('title,inBody,expData',
                             get_InstancePay_yaml_data(data_path + 'InstancePayCase.yaml'))
    @allure.story('包年包月实例订单付费接口')
    @allure.title("{title}")
    def test_pag_instance(self, title, inBody, expData, create_prepay_order):
        resData = InstancePay().instance_pay(inData={'order_uuid': create_prepay_order})
        print(resData)
        self.define_assert(resData, expData)


if __name__ == '__main__':
    TestCreatePagInstance().test_pag_instance()
