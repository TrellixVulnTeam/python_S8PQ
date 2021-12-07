import pytest
from common.Read_Yaml import get_login_yaml_data
from config.login import Login
from config_path import get_login_yaml_path


class TestLogin:
    # 调用业务代码
    @pytest.mark.parametrize('inBody,expData', get_login_yaml_data(get_login_yaml_path()))  # 数据驱动方法
    def test_login(self, inBody, expData):
        resData = Login().login(inData=inBody, mode=False)
        assert resData['msg'] == expData['msg']


if __name__ == '__main__':
    pytest.main(["LoginCase.py", "-vs", "--alluredir", "../report/reportallure/",
                 '-W', 'ignore:Module already imported:pytest.PytestWarning'])
