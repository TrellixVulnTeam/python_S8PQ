import os
import sys
import allure
import config
from common import Assert, Consts, Random_number
from common.Logs import Log
from common.Request import RequestsHandler
from common.Return_Response import dict_style
from Auth import AutoDL_auth
from config import adss

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger


@allure.feature("注册模块")
class TestRegister:
    """
    测试注册功能接口
    """
    @allure.story("参数填写正确，注册成功")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("正常注册账号")
    def test_Register(self):
        # 获取函数名
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        num = Random_number.main()
        url = base_url + 'register'
        data = {
            "password": "123456Aa",
            "phone": num,
            "v_code": "666666"
        }
        # 授权
        token = AutoDL_auth.change_ticket()
        headers = {"Authorization": token}
        r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
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

    @allure.story("参数填写不正确，注册失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("不填写手机号")
    def test_No_Num(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        num = Random_number.main()
        url = base_url + 'register'
        data = {
            "phone": num,
            "v_code": "666666"
        }
        token = AutoDL_auth.change_ticket()
        # 请求头 授权
        headers = {"Authorization": token}
        r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
        code1 = r.status_code
        str_response = r.content.decode()
        json_response = dict_style(str_response)
        test_assert.assert_code(code1, 200)
        test_assert.assert_body(json_response, 'msg', '请求参数错误')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，注册失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("手机号填写10位")
    def test_Wrong_Num(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        url = base_url + 'register'
        data = {
            "password": "123456Aa",
            "phone": "188010533",
            "v_code": "666666"
        }
        token = AutoDL_auth.change_ticket()
        # 请求头 授权
        headers = {"Authorization": token}
        r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
        code1 = r.status_code
        str_response = r.content.decode()
        json_response = dict_style(str_response)
        test_assert.assert_code(code1, 200)
        test_assert.assert_body(json_response, 'msg', '手机号格式错误')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，注册失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("手机号有非法字符")
    def test_Illegal_Character(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        url = base_url + 'register'
        data = {
            "password": "123456Aa",
            "phone": "1880105330！",
            "v_code": "666666"
        }
        token = AutoDL_auth.change_ticket()
        # 请求头 授权
        headers = {"Authorization": token}
        r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
        code1 = r.status_code
        str_response = r.content.decode()
        json_response = dict_style(str_response)
        test_assert.assert_code(code1, 200)
        test_assert.assert_body(json_response, 'msg', '手机号格式错误')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，注册失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("已经注册过的手机号")
    def test_Registered_Num(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        url = base_url + 'register'
        data = {
            "password": "123456Aa",
            "phone": "18801053303",
            "v_code": "666666"
        }
        token = AutoDL_auth.change_ticket()
        # 请求头 授权
        headers = {"Authorization": token}
        r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
        code1 = r.status_code
        str_response = r.content.decode()
        json_response = dict_style(str_response)
        test_assert.assert_code(code1, 200)
        test_assert.assert_body(json_response, 'msg', '手机号已注册，请登录')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，注册失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("密码输入7位")
    def test_Pwd_Error(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        num = Random_number.main()
        url = base_url + 'register'
        data = {
            "password": "123456A",
            "phone": num,
            "v_code": "666666"
        }
        token = AutoDL_auth.change_ticket()
        # 请求头 授权
        headers = {"Authorization": token}
        r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
        code1 = r.status_code
        str_response = r.content.decode()
        json_response = dict_style(str_response)
        test_assert.assert_code(code1, 200)
        test_assert.assert_body(json_response, 'msg', '')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，注册失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("密码没有大写")
    def test_Pwd_No_Capitalization(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        num = Random_number.main()
        url = base_url + 'register'
        data = {
            "password": "123456aa",
            "phone": num,
            "v_code": "666666"
        }
        token = AutoDL_auth.change_ticket()
        # 请求头 授权
        headers = {"Authorization": token}
        r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
        code1 = r.status_code
        str_response = r.content.decode()
        json_response = dict_style(str_response)
        test_assert.assert_code(code1, 200)
        test_assert.assert_body(json_response, 'msg', '')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，注册失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("不输入密码")
    def test_No_Pwd(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        num = Random_number.main()
        url = base_url + 'register'
        data = {
            "phone": num,
            "v_code": "666666"
        }
        token = AutoDL_auth.change_ticket()
        # 请求头 授权
        headers = {"Authorization": token}
        r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
        code1 = r.status_code
        str_response = r.content.decode()
        json_response = dict_style(str_response)
        test_assert.assert_code(code1, 200)
        test_assert.assert_body(json_response, 'msg', '请求参数错误')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，注册失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("验证码输入错误")
    def test_CodeError(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        num = Random_number.main()
        url = base_url + 'register'
        data = {
            "password": "123456Aa",
            "phone": num,
            "v_code": "12345"
        }
        token = AutoDL_auth.change_ticket()
        # 请求头 授权
        headers = {
            "Authorization": token
        }
        r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
        code1 = r.status_code
        str_response = r.content.decode()
        json_response = dict_style(str_response)
        test_assert.assert_code(code1, 200)
        test_assert.assert_body(json_response, 'msg', '验证码无效，请重新获取')
        Consts.RESULT_LIST.append('pass')

    @allure.story("参数填写不正确，注册失败")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("不输入验证码")
    def test_No_Code(self):
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s：\n", def_name)
        base_url = config.adss.server_ip()
        num = Random_number.main()
        url = base_url + 'register'
        data = {
            "password": "123456Aa",
            "phone": num,
        }
        token = AutoDL_auth.change_ticket()
        # 请求头 授权
        headers = {
            "Authorization": token
        }
        r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
        code1 = r.status_code
        str_response = r.content.decode()
        json_response = dict_style(str_response)
        test_assert.assert_code(code1, 200)
        test_assert.assert_body(json_response, 'msg', '请求参数错误')
        Consts.RESULT_LIST.append('pass')


if __name__ == '__main__':

    TestRegister().test_Register()
