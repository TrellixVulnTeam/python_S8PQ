from pprint import pprint

import config
from Auth.AutoDL_auth import get_token
from common.BaseApi import BaseApi
from common.Request import RequestsHandler
from config.adss import server_ip


class Recharge(BaseApi):

    def wx_recharge(self, inData):
        base_url = config.adss.server_ip()
        url = base_url + 'wallet/recharge/wx'
        token = get_token()
        header = {'Authorization': token}
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        print(res.json())
        return res.json()

    def alipay_recharge(self, inData):
        base_url = config.adss.server_ip()
        url = base_url + 'wallet/recharge/alipay'
        token = get_token()
        header = {'Authorization': token}
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        print(res.json())
        return res.json()

    # 轮循查看是否充值成功
    def wallt_recharge(self):
        base_url = config.adss.server_ip()
        url = base_url + 'wallet/recharge'
        token = get_token()
        header = {'Authorization': token}
        payload = {
            'recharge_uuid': self.wx_recharge({"asset": 100})
        }
        res = RequestsHandler().get_Req(url, params=payload, headers=header)
        print(res.json())
        return res


if __name__ == '__main__':
    # Recharge().alipay_recharge({"asset": 1000})
    Recharge().wallt_recharge()
