import os
import sys
import pytest, allure

from common.Assert import BaseAssert
from common.Logs import Log
from common.Return_Response import dict_style
from libs.login import Login
from utils.handle_path import data_path
from utils.handle_yaml import get_yamlCase_data

file = os.path.basename(sys.argv[0])
print(file)
log = Log(file)
logger = log.Logger


# @allure.epic('AutoDL')
@allure.feature('登录模块')
class TestLogin(BaseAssert):
    # 调用业务代码
    @allure.story('登录接口')  # 接口名称
    # @allure.title('登录用例')  # 用例标题
    @pytest.mark.parametrize('title,inBody,expData', get_yamlCase_data(data_path + '\\LoginCase.yaml'))  # 数据驱动方法
    @allure.title("{title}")
    def test_login(self, title, inBody, expData):
        # 1- 调用业务层封装的接口代码
        resData = Login().login(inData=inBody, getToken=False)
        print("请求参数:", inBody)
        print("预期结果:", expData)
        print("实际结果：", resData)
        self.define_assert(resData, expData)


if __name__ == '__main__':
    pytest.main(["test_LoginCase.py", "-vs", "--alluredir", "../report/reportallure/",
                 '-W', 'ignore:Module already imported:pytest.PytestWarning'])
