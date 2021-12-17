import os
import sys
import time

import pytest
from common import Shell
from common.Logs import Log

if __name__ == "__main__":
    file = os.path.basename(sys.argv[0])
    log = Log(file)
    logger = log.Logger

    # 运行整个目录 pytest.main(['../cases', '--html=../report/report.html'])
    # logger.info("开始执行脚本") >pytest E:\project\Xiaoniu_Api_Rili\Run\run_all_case.py

    try:
        print("开始执行脚本")
        logger.info("==================================" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                         time.localtime()) + "===================================")
        pytest.main(
            ['../cases/RegisterCase.py', '../cases/LoginCase.py', "--alluredir",  "../report/reportallure/","--clean-alluredir",
             '-W', 'ignore:Module already imported:pytest.PytestWarning'])
        # pytest.main(
        #     ['../cases', '-vs', "--alluredir", "../report/reportallure/", "--clean-alluredir",
        #      '-W', 'ignore:Module already imported:pytest.PytestWarning'])

        print("脚本执行完成")
    except Exception as e:
        logger.error("脚本批量执行失败！", e)
        print("脚本批量执行失败！", e)

    try:
        shell = Shell.Shell()
        cmd = 'allure generate %s -o %s --clean' % ('../report/reportallure/', '../report/reporthtml')
        # logger.info("开始执行报告生成")
        print("开始执行报告生成")
        shell.invoke(cmd)
        # logger.info("报告生成完毕")
        print("报告生成完毕")
    except Exception as e:
        print("报告生成失败，请重新执行", e)
        # logger.error("报告生成失败，请重新执行", e)
        # logger.error('执行用例失败，请检查环境配置')
        raise

    time.sleep(3)
    # mail()
# allure generate ./reportallure/ -o ./reporthtml/ --clean
