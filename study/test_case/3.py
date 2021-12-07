import pytest
import requests
from comm.Request import RequestsHandler
from comm.read_yaml_Util import read_yaml


class TestClass_1:

    # @pytest.mark.parametrize(name, value)
    @pytest.mark.parametrize("case_info", read_yaml())
    def test_register(self, case_info):
        # print(case_info)
        # print(case_info['name'])
        # print(case_info['request']['url'])
        # print(case_info['request']['data'])
        res = RequestsHandler().post_Req((case_info['request']['url']), (case_info['request']['data']))
        print(res.json())
        print(case_info['validata'])


if __name__ == '__main__':
    pytest.main(["-vs", "3.py"])
