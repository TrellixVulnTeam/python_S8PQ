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
log = Log(file)
logger = log.Logger


@allure.epic('AutoDL')
@allure.feature('登录模块')
class TestLogin(BaseAssert):
    # 调用业务代码

    @pytest.mark.parametrize('title,inBody,expData', get_yamlCase_data(data_path + 'LoginCase.yaml'))  # 数据驱动方法
    @allure.story('登录接口')
    @allure.title("{title}")  # 用例标题
    def test_login(self, title, inBody, expData):
        # 1- 调用业务层封装的接口代码
        resData = Login().login(inData=inBody)
        logger.info(f'当前用例名称：{title}')
        logger.info(f'当前测试用例请求参数：{inBody}')
        logger.info(f'当前用例预期结果：{expData}')
        logger.info(f'当前用例实际结果：{resData}\n')
        try:
            self.define_assert(resData, expData)
        except AssertionError as e:
            logger.error(f'用例执行失败{e}')
            raise e


if __name__ == '__main__':
    pytest.main(["test_LoginCase.py", "-vs", "--alluredir", "../report/reportallure/",
                 '-W', 'ignore:Module already imported:pytest.PytestWarning'])
