import os
import sys
from datetime import time
import time

import allure
import requests
import config
from Auth.AutoDL_auth import get_captcha
from common import Assert, Consts
from common.Logs import Log
from common.Return_Response import dict_style
from config import adss

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger


def right_login():
    cap_id, cap_val = get_captcha()
    base_url = config.adss.server_ip()
    url = base_url + 'login'
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val, "phone": "18801053303",
                                     "password": "123456Aa"}, headers=headers)
    print(r.json())


def sendWrongLoginRequest():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    # logger.info("开始执行脚本%s：\n", def_name)
    cap_id, cap_val = get_captcha()
    base_url = config.adss.server_ip()
    url = base_url + 'login'
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val, "password": "132542",
                                     "phone": "15841593108"}, headers=headers)
    # print(r.json())
    # 获取接口返回信息
    str_response = r.content.decode()
    # 读取json
    json_response = dict_style(str_response)
    # 校验状态码是否是200
    # test_assert.assert_code(code1, 200)
    # 校验返回信息是否与预期信息一致
    # test_assert.assert_body(json_response, 'msg', '连续超过 6 次错误，请于 5 分钟后重新登录')
    # Consts.RESULT_LIST.append('pass')
    if json_response["msg"] == "连续超过 6 次错误，请于 5 分钟后重新登录":
        return True, json_response["msg"]
    else:
        return False, json_response["msg"]


@allure.feature("登录模块")
class TestLogin:
    @allure.story("账号密码填写正确，登陆成功")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("正常登录账号")
    def test_login(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        cap_id, cap_val = get_captcha()
        base_url = config.adss.server_ip()
        url = base_url + 'login'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val, "phone": "18801053303",
                                         "password": "a753c776ff3ed4fefa2af948af87448910153281"}, headers=headers)
        code1 = r.status_code
        # 获取接口返回信息
        str_response = r.content.decode()
        # 读取json
        json_response = dict_style(str_response)
        # 校验状态码是否是200
        test_assert.assert_code(code1, 200)
        # 校验返回信息是否与预期信息一致
        test_assert.assert_body(json_response, 'msg', '')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，登录失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("不输入账号进行登录")
    def test_no_num(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        cap_id, cap_val = get_captcha()
        base_url = config.adss.server_ip()
        url = base_url + 'login'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val,
                                         "password": "123456Aa"}, headers=headers)
        code1 = r.status_code
        # 获取接口返回信息
        str_response = r.content.decode()
        # 读取json
        json_response = dict_style(str_response)
        # 校验状态码是否是200
        test_assert.assert_code(code1, 200)
        # 校验返回信息是否与预期信息一致
        test_assert.assert_body(json_response, 'msg', '请求参数错误')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，登录失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("输入不存在的账号")
    def test_nonexistent_num(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        cap_id, cap_val = get_captcha()
        base_url = config.adss.server_ip()
        url = base_url + 'login'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val,
                                         "phone": "18801057863"}, headers=headers)
        print(r.json())
        code1 = r.status_code
        # 获取接口返回信息
        str_response = r.content.decode()
        # 读取json
        json_response = dict_style(str_response)
        # 校验状态码是否是200
        test_assert.assert_code(code1, 200)
        # 校验返回信息是否与预期信息一致
        test_assert.assert_body(json_response, 'msg', '请求参数错误')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，登录失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("账号有特殊字符")
    def test_Num_Illegal_Character(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        cap_id, cap_val = get_captcha()
        base_url = config.adss.server_ip()
        url = base_url + 'login'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val, "password": "123456Aa",
                                         "phone": "188888888$!"}, headers=headers)
        print(r.json())
        code1 = r.status_code
        # 获取接口返回信息
        str_response = r.content.decode()
        # 读取json
        json_response = dict_style(str_response)
        # 校验状态码是否是200
        test_assert.assert_code(code1, 200)
        # 校验返回信息是否与预期信息一致
        test_assert.assert_body(json_response, 'msg', '手机号或密码错误，请重试')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，登录失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("输入10位手机号")
    def test_wrong_num(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        cap_id, cap_val = get_captcha()
        base_url = config.adss.server_ip()
        url = base_url + 'login'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val, "password": "123456Aa",
                                         "phone": "1880105378"}, headers=headers)
        print(r.json())
        code1 = r.status_code
        # 获取接口返回信息
        str_response = r.content.decode()
        # 读取json
        json_response = dict_style(str_response)
        # 校验状态码是否是200
        test_assert.assert_code(code1, 200)
        # 校验返回信息是否与预期信息一致
        test_assert.assert_body(json_response, 'msg', '手机号或密码错误，请重试')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，登录失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("输入10位手机号")
    def test_wrong_num(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        cap_id, cap_val = get_captcha()
        base_url = config.adss.server_ip()
        url = base_url + 'login'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val, "password": "123456Aa",
                                         "phone": "1880105363"}, headers=headers)
        print(r.json())
        code1 = r.status_code
        # 获取接口返回信息
        str_response = r.content.decode()
        # 读取json
        json_response = dict_style(str_response)
        # 校验状态码是否是200
        test_assert.assert_code(code1, 200)
        # 校验返回信息是否与预期信息一致
        test_assert.assert_body(json_response, 'msg', '手机号或密码错误，请重试')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，登录失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("不填写密码进行登录")
    def test_no_pwd(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        cap_id, cap_val = get_captcha()
        base_url = config.adss.server_ip()
        url = base_url + 'login'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val,
                                         "phone": "1880105344"}, headers=headers)
        print(r.json())
        code1 = r.status_code
        # 获取接口返回信息
        str_response = r.content.decode()
        # 读取json
        json_response = dict_style(str_response)
        # 校验状态码是否是200
        test_assert.assert_code(code1, 200)
        # 校验返回信息是否与预期信息一致
        test_assert.assert_body(json_response, 'msg', '请求参数错误')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，登录失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("密码输入6位")
    def test_wrong_pwd(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        cap_id, cap_val = get_captcha()
        base_url = config.adss.server_ip()
        url = base_url + 'login'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val, "password": "123456",
                                         "phone": "1880105337"}, headers=headers)
        print(r.json())
        code1 = r.status_code
        # 获取接口返回信息
        str_response = r.content.decode()
        # 读取json
        json_response = dict_style(str_response)
        # 校验状态码是否是200
        test_assert.assert_code(code1, 200)
        # 校验返回信息是否与预期信息一致
        test_assert.assert_body(json_response, 'msg', '手机号或密码错误，请重试')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，登录失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("不填账号和密码进行登录")
    def test_no_num_pwd(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        cap_id, cap_val = get_captcha()
        base_url = config.adss.server_ip()
        url = base_url + 'login'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(url=url, json={"captcha_id": cap_id, "captcha_value": cap_val,
                                         }, headers=headers)
        print(r.json())
        code1 = r.status_code
        # 获取接口返回信息
        str_response = r.content.decode()
        # 读取json
        json_response = dict_style(str_response)
        # 校验状态码是否是200
        test_assert.assert_code(code1, 200)
        # 校验返回信息是否与预期信息一致
        test_assert.assert_body(json_response, 'msg', '请求参数错误')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，登录失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("密码输入6次错误")
    def test_wrong_pwd(self):
        def_name = sys._getframe().f_code.co_name
        # test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        forbid_5_min = False
        retry_times = 0

        for i in range(10):
            forbid_5_min, msg = sendWrongLoginRequest()
            logger.info("login result: times=%d, msg=%s.\n", i, msg)

            if not forbid_5_min:
                retry_times += 1

            # if forbid_5_min:
            #     break

        if not forbid_5_min:
            logger.error("Error! 没有触发等待 5 分钟")
            return

        if retry_times > 6:
            logger.error("Error! 没有在第6次错误禁止登录, 次数为", retry_times)

        if right_login():
            logger.error("ERROR!!!!")

    @allure.story("短信登录")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("手机号和短信验证码填写正确，正常登录")
    def test_code_login(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        url = base_url + 'fast_login'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(url=url, json={"phone": "18801053303", "v_code": "666666"}, headers=headers)
        print(r.json())
        code1 = r.status_code
        # 获取接口返回信息
        str_response = r.content.decode()
        # 读取json
        json_response = dict_style(str_response)
        # 校验状态码是否是200
        test_assert.assert_code(code1, 200)
        # 校验返回信息是否与预期信息一致
        test_assert.assert_body(json_response, 'msg', '')
        Consts.RESULT_LIST.append('pass')

