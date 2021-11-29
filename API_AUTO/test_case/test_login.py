import sys

import pytest
import allure,os
from Auth.AutoDL_auth import get_captcha
from common.Read_Yaml import get_yaml_data
from common.login import Login
from common.Logs import Log
from path import get_yaml_path
# file = os.path.basename(sys.argv[0])
# log = Log(file)
# logger = log.Logger

# # 执行用例
# # 1- 获取用例数据
#
# case = get_yaml_data('../test_data/test_study.yaml')[1]
# data = case['data']
# resp = case['resp']
#
# # 2- 调用接口方法--获取响应数据
# cap_id, cap_val = get_captcha()
# resContent = {"phone": data['phone'], "password": data['password'], "captcha_id": cap_id, "captcha_value": cap_val}
# respData = Login().login(resContent, False)
#
# # 3- 断言  实际结果与预期结果做对比
# if respData['msg'] == resp['msg']:
#     print("case1>>>>>pass")
# else:
#     print("case1>>>>>fail")


class TestLogin:
    # 调用业务代码
    @pytest.mark.parametrize('inBody,expData', get_yaml_data(get_yaml_path()))  # 数据驱动方法
    def test_login(self, inBody, expData):
        resData = Login().login(inData=inBody, mode=False)
        assert resData['msg'] == expData['msg']


if __name__ == '__main__':
    pytest.main(["test_login.py", "-vs", "--alluredir", "../report/reportallure/",
                 '-W', 'ignore:Module already imported:pytest.PytestWarning'])
#     os.system("allure serve ../report/reporthtml")
#     """
#         1.生成报告所需文件
#         2.使用一些工具打开可视化报告
#     """
