import os
import sys
import pytest, allure

from common.Assert import BaseAssert
from common.Logs import Log
from common.Return_Response import dict_style
from libs.new_login import Login
from utils.handle_path import data_path
from utils.handle_yaml import get_yamlCase_data


@allure.epic('AutoDL')
@allure.feature('登录模块')
class TestLogin(BaseAssert):
    # 调用业务代码

    @pytest.mark.parametrize('title,data,expData', get_yamlCase_data(data_path + 'LoginCase.yaml'))  # 数据驱动方法
    @allure.story('登录接口')
    @allure.title("{title}")  # 用例标题
    def test_login(self, title, data, expData):
        # 1- 调用业务层封装的接口代码
        resData = Login().login(data)
        self.define_assert(resData, expData)


if __name__ == '__main__':
    pytest.main(["test_LoginCase.py", "-vs", "--alluredir", "../report/reportallure/",
                 '-W', 'ignore:Module already imported:pytest.PytestWarning'])
