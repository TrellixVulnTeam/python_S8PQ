import sys

import pytest

from common import Assert
from common.Read_Yaml import get_register_yaml_data
from config.regitster import Register
from config_path import get_login_yaml_path


class TestRegister:
    @pytest.mark.parametrize('inBody,expData', get_register_yaml_data())
    # 注册
    def test_register(self, inBody, expData):
        print("test-----------------------------------")
        print("inBody:", inBody)
        print("expData:", expData)
        resData = Register().register(inData=inBody)
        assert resData['msg'] == expData['msg']


if __name__ == '__main__':
    pytest.main('-vs', 'test_RegisterCase.py')
