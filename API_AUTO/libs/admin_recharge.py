#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/7/6 15:28
# @Author : ZhangTy
# @File : admin_recharge.py

def test_admin_recharge():
    token = change_ticket()
    url = 'https://test.autodl.com:33443/admin/v1/wallet/recharge'
    token1 = {
        "Authorization": token
    }
    # print(token1)
    req = {"asset": 1000000000000, "id": 241}
    r = requests.post(url=url, json=req, headers=token1)
    print(r.json())