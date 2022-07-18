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


@allure.epic('AutoDL')
@allure.feature('注册模块')
class TestRegister(BaseAssert):

    @pytest.mark.parametrize('title,data,expData', get_register_yaml_data(data_path + 'RegisterCase.yaml'))
    @allure.story('注册接口')
    @allure.title("{title}")
    def test_register(self, title, data, expData):
        resData = Register().register(data)
        self.define_assert(resData, expData)


if __name__ == '__main__':
    pytest.main('-vs', 'test_RegisterCase.py')
