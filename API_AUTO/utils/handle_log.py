#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/3/25 15:32
# @Author : ZhangTy
# @File : handle_log.py


import os
import logging


class HandleLog:
    def __init__(self):
        self.logger = logging.getLogger()

        format_data = logging.Formatter(
            '%(asctime)s -  级别：%(levelname)s - 模块：%(module)s - 函数名：%(funcName)s - 信息：%(message)s - 行号：%(lineno)d',
            datefmt='%Y/%m/%d %H:%M:%S')

        # 日志控制台输出
        console = logging.StreamHandler()

        # 日志文件写入
        path = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), 'log')
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)
        filename = os.path.join(path, 'logs')
        file_write = logging.FileHandler(
            filename=filename, mode='a+', encoding='utf-8')

        # 将日志处理器的设置成Formatter提供的格式化
        console.setFormatter(format_data)
        file_write.setFormatter(format_data)

        # 把日志处理去绑定到日志记录器上
        self.logger.addHandler(file_write)
        self.logger.addHandler(console)

    def get_log(self):
        return self.logger


handle_log = HandleLog().get_log()


if __name__ == '__main__':
    handle_log.info('我是info级别')
    handle_log.debug('我是debug级别')
    handle_log.warning('我是warning级别')
    handle_log.error('我是error级别')
    handle_log.critical('我是critical级别')