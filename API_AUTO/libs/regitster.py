from pprint import pprint
import config.adss
from common import Random_number
from common.Request import RequestsHandler


class Register:

    def register(self, inData):
        base_url = config.adss.server_ip()
        url = base_url + 'register'
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload)
        return res.json()


if __name__ == '__main__':
    num = Random_number.main()
    res = Register().register({"password": "123456Aa", "phone": num, "v_code": "666666"})
    pprint(res)
