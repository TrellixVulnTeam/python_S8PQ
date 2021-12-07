from pprint import pprint
import json
import config.adss
from common import Request
from common.Request import RequestsHandler
from data import Random_number


class Register:

    def register(self, inData, mode=False):
        base_url = config.adss.server_ip()
        url = base_url + 'register'
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload)
        return res


if __name__ == '__main__':
    num = Random_number.main()
    res = Register().register({"password": "123456Aa", "phone": num, "v_code": "666666"})
    pprint(res.json())
