from pprint import pprint

import pytest
import requests

import config.adss
from comm.AutoDL_auth import change_ticket
from comm.Request import RequestsHandler


class InstanceCreat:

    def creat_instance(self):
        base_url = config.adss.server_ip()
        url = base_url + 'instance'
        token = change_ticket()
        header = {'Authorization': token}
        payload = {
            "date_from": "",
            "date_to": "",
            "page_index": 1,
            "page_size": 20
        }
        res = RequestsHandler().get_Req(url, params=payload, headers=header)
        pprint(res.json())
        # for item in res.json():
        #     print(res.json()[item])
        return res.json()


if __name__ == '__main__':
    InstanceCreat().creat_instance()
