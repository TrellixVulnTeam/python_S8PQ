import hashlib
import inspect
import pprint
import sys

import requests
from Auth.AutoDL_auth import get_captcha
import config
from common import Assert
from common.Request import RequestsHandler
from common.Return_Response import dict_style
from config import adss
from common.Assert import Assertions
from utils.handle_data import get_sha1


class Login:

    def login(self, inData, getToken=False):  # 登录方法
        base_url = config.adss.server_ip()
        # 字典名[键名] = 新的值   字典修改值操作
        pwd = inData["password"]
        inData["password"] = get_sha1(pwd)
        url = base_url + 'new_login'
        # 参数
        payload = inData

        # 请求
        """
        data ----表单格式
        json----json
        files----文件上传接口
        params----参数会放到url路径里
        """
        resp = RequestsHandler().post_Req(url, json=payload)
        # str_response = resp.content.decode()
        # json_response = dict_style(str_response)
        # test_assert.assert_body(json_response, 'msg', '')
        # 查看响应
        if getToken:
            return resp.json()["data"]["ticket"]
        else:
            return resp.json()


if __name__ == '__main__':
    res = Login().login(
        {"phone": "18801053303", "password": "123456Aa", "picture_id": "", "v_code": ""})
    pprint.pprint(res)
