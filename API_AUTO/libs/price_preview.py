#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/15 16:39
# @Author : ZhangTy
# @File : price_preview.py
import config.adss
from Auth.AutoDL_auth import get_token
from common.Request import RequestsHandler
from libs.Instance_info import get_gpu_idle_num


class PreviewPrice:
    # 获取包年包月机器价格
    def get_daily_price(self):
        base_url = config.adss.server_ip()
        url = base_url + 'order/price/preview'
        token = get_token()
        header = {'Authorization': token}
        payload = {"charge_type": "daily",
                   "coupon_id_list": [],
                   "duration": 1,
                   "expand_data_disk": 0,
                   "machine_id": get_gpu_idle_num(),
                   "num": 1}
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        print(res.json())

    # 获取按量计费机器价格
    def get_payg_price(self):
        base_url = config.adss.server_ip()
        url = base_url + 'order/price/preview'
        token = get_token()
        header = {'Authorization': token}
        payload = {"charge_type": "payg",
                   "coupon_id_list": [],
                   "duration": 1,
                   "expand_data_disk": 0,
                   "machine_id": get_gpu_idle_num(),
                   "num": 1}
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        print(res.json())


if __name__ == '__main__':
    PreviewPrice().get_daily_price()
    PreviewPrice().get_payg_price()
