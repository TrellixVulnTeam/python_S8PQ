import traceback

import allure
import pytest

from common.Assert import log, BaseAssert
from libs.regitster import Register
from utils.handle_path import data_path
from utils.handle_yaml import get_register_yaml_data


class TestRegister(BaseAssert):

    @allure.story('注册接口')  # 接口名称
    # @allure.title('注册用例')  # 用例标题
    @pytest.mark.parametrize('title,inBody,expData', get_register_yaml_data(data_path + '\\RegisterCase.yaml'))
    @allure.title("{title}")
    def test_register(self, title, inBody, expData):
        resData = Register().register(inData=inBody)
        print("请求参数:", inBody)
        print("预期结果:", expData)
        print("实际结果：", resData)
        self.define_assert(resData, expData)


if __name__ == '__main__':
    pytest.main('-vs', 'test_RegisterCase.py')
