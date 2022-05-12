#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/15 17:08
# @Author : ZhangTy
# @File : get_balance.py
from Auth.AutoDL_auth import get_token
from config.adss import server_ip
from common.Request import RequestsHandler


class Balance:
    # 获取用户余额
    def get_wallet_balance(self):
        base_url = server_ip()
        url = base_url + 'wallet/balance'
        token = get_token()
        header = {'Authorization': token}
        res = RequestsHandler().get_Req(url, params='', headers=header)
        print(res.json())
        return res.json()


if __name__ == '__main__':
    Balance().get_wallet_balance()
