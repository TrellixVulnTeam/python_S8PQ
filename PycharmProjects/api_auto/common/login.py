import hashlib
import pprint
import requests
from Auth.AutoDL_auth import get_captcha
import config
from config import adss


def get_sha1(psw):
    # 实例化对象
    md5 = hashlib.sha1()
    # 调用加密方法直接加密
    md5.update(psw.encode("utf-8"))
    # 返回md5加密的结果
    return md5.hexdigest()


class Login:

    def login(self, inData, mode=False):  # 登录方法
        base_url = config.adss.server_ip()
        # 字典名[键名] = 新的值   字典修改值操作
        pwd = inData["password"]
        inData["password"] = get_sha1(pwd)
        url = base_url + 'login'
        # 参数
        payload = inData

        # 请求
        """
        data ----表单格式
        json----json
        files----文件上传接口
        params----参数会放到url路径里
        """
        resp = requests.post(url, json=payload)
        # 查看响应
        if mode:
            return resp.json()["data"]["ticket"]
        else:
            return resp.json()


if __name__ == '__main__':
    cap_id, cap_val = get_captcha()
    res = Login().login(
        {"phone": "18801053303", "password": "123456Aa", "captcha_id": cap_id, "captcha_value": cap_val})
    pprint.pprint(res)
