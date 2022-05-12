import os
import sys
import allure
import requests

from Auth.AutoDL_auth import get_captcha, change_ticket


# 管理员充值
def test_admin_recharge():
    # def_name = sys._getframe().f_code.co_name
    # test_assert = Assert.Assertions(def_name)
    # logger.info("开始执行脚本%s：\n", def_name)
    token = change_ticket()
    url = 'https://test.autodl.com:33443/admin/v1/wallet/recharge'
    token1 = {
        "Authorization": token
    }
    # print(token1)
    req = {"asset": 200000, "id": 3}
    r = requests.post(url=url, json=req, headers=token1)
    print(r.json())


if __name__ == '__main__':
#     wx_msg_push()
    test_admin_recharge()
# code1 = r.status_code
# # 获取接口返回信息
# str_response = r.content.decode·()
# # 读取json
# json_response = dict_style(str_response)
# 校验状态码是否是200
# test_assert.assert_code(code1, 200)
# 校验返回信息是否与预期信息一致
# test_assert.assert_body(json_response, 'msg', '连续超过 5 次错误，请于 15 分钟后重新登录')
# Consts.RESULT_LIST.append('pass')


# # 邀请注册
# def test_register_invited():
#     def_name = sys._getframe().f_code.co_name
#     test_assert = Assert.Assertions(def_name)
#     logger.info("开始执行脚本%s：\n", def_name)
#     token = change_ticket()
#     url = 'https://test.autodl.com:30098/api/v1/register/invited'
#     token1 = {
#         "Authorization": token
#     }
#     print(token1)
#     req = {
#         "invite_code": "487686b5-637f-4d99-8202-7c0b29fa322d",
#         "password": "123456aa",
#         "phone": "18801053302",
#         "v_code": "666666"
#     }
#     r = requests.post(url=url, json=req, headers=token1)
#     print(r.json())

#
# def test_wx_phone_bind():
#     def_name = sys._getframe().f_code.co_name
#     test_assert = Assert.Assertions(def_name)
#     logger.info("开始执行脚本%s：\n", def_name)
#     token = change_ticket()
#     url = 'https://test.autodl.com:30098/api/v1/wx/phone/bind'
#     token1 = {
#         "Authorization": token
#     }
#     print(token1)
#     req = {
#         "open_id": "qwejkaldhjsa",
#         "phone": "18801053300",
#         "v_code": "666666"
#     }
#     r = requests.post(url=url, json=req, headers=token1)
#     print(r.json())
