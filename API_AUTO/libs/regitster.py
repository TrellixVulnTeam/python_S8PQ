from pprint import pprint
import config.adss
from common import Random_number
from common.Request import RequestsHandler
from common.BaseApi import BaseApi


class Register(BaseApi):

    def register(self, data):
        resp = self.request_send(data)
        return resp


if __name__ == '__main__':
    num = Random_number.main()
    res = Register().register({"phone_area": "+86", "password": "123456Aa", "phone": num, "v_code": "666666"})
    pprint(res)
