import pytest, allure
from common.Read_Yaml import get_login_yaml_data
from config.login import Login
from config_path import get_login_yaml_path
from practice_test.test2 import BaseAssert


@allure.feature('登录模块')
class TestLogin:
    # 调用业务代码
    @allure.story('登录接口')
    @pytest.mark.parametrize('inBody,expData', get_login_yaml_data())  # 数据驱动方法
    def test_login(self, inBody, expData):
        resData = Login().login(inData=inBody, mode=False)
        print(resData)
        assert resData['msg'] == expData['msg']


if __name__ == '__main__':
    pytest.main(["test_LoginCase.py", "-vs", "--alluredir", "../report/reportallure/",
                 '-W', 'ignore:Module already imported:pytest.PytestWarning'])
