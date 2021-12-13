import pytest
from common.Read_Yaml import get_register_yaml_data
from config.regitster import Register
from config_path import get_login_yaml_path


class TestRegister:
    # 调用业务代码
    @pytest.mark.parametrize('inBody,expData', get_register_yaml_data())
    def test_register(self, inBody, expData):
        resData = Register().register(inData=inBody)
        assert resData['msg'] == expData['msg']


if __name__ == '__main__':
    pytest.main('-vs', 'RegisterCase.py')
