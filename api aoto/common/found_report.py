import os
# !/usr/bin/python
# coding: UTF-8
import time


def new_report(report):
    lists = os.listdir(report)  # 列出目录的下所有文件和文件夹保存到lists

    print(list)

    lists.sort(key=lambda fn: os.path.getmtime(report + "\\" + fn))  # 按时间排序

    file_new = os.path.join(report, lists[-1])  # 获取最新的文件保存到file_new

    print(file_new)

    return file_new


if __name__ == "__main__":

    test_path = "D:\\test\\vmware.log"  # 目录地
    new_report = new_report(test_path)
    print(new_report)
