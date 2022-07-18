from pprint import pprint

import config
from Auth.AutoDL_auth import get_token
from common.BaseApi import BaseApi
from common.Request import RequestsHandler
from config.adss import server_ip
from libs.new_login import Login


class Recharge(BaseApi):

    def wx_recharge(self, data):
        resp = self.request_send(data)
        return resp

    def alipay_recharge(self, data):
        resp = self.request_send(data)
        return resp

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
    # 登录
    ticket = Login().login({"phone": "18801053303", "password": "123456aa", "picture_id": "", "v_code": ""})
    # 用ticket换token
    token = Login().get_token({"ticket": ticket}, token=True)
    Recharge(token).wx_recharge({"asset": 100000, "id": "51036"})
    # Recharge().wallt_recharge()
