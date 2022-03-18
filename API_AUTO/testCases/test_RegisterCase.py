import os
import sys
import traceback

import allure
import pytest

from common.Assert import BaseAssert
from libs.regitster import Register
from utils.handle_path import data_path
from utils.handle_yaml import get_register_yaml_data
from common.Logs import Log

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger


@allure.feature('注册模块')
class TestRegister(BaseAssert):

    @allure.story('注册接口')  # 接口名称
    # @allure.title('注册用例')  # 用例标题
    @pytest.mark.parametrize('title,inBody,expData', get_register_yaml_data(data_path + 'RegisterCase.yaml'))
    @allure.title("{title}")
    def test_register(self, title, inBody, expData):
        resData = Register().register(inData=inBody)
        # yaml_detail = get_yamlCase_detail_data(data_path + '\\RegisterCase.yaml')
        logger.info(f'当前用例名称：{title}')
        logger.info(f'当前测试用例请求参数：{inBody}')
        logger.info(f'当前用例预期结果：{expData}')
        logger.info(f'当前用例实际结果：{resData}\n')
        try:
            self.define_assert(resData, expData)
            # logger.info(resData)
        except AssertionError as e:
            logger.error(f'用例执行失败{e}')
            raise e


if __name__ == '__main__':
    pytest.main('-vs', 'test_RegisterCase.py')
