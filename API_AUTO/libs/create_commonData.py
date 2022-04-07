#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/2 15:05
# @Author : ZhangTy
# @File : create_commonData.py
import config
from Auth.AutoDL_auth import change_ticket
from common.Request import RequestsHandler
from config.adss import server_ip


class CommonData:

    def creat_CommonData(self, inData):
        # base_url = config.adss.server_ip()
        url = 'https://test.autodl.com:33443/api/v1/public_data'
        token = change_ticket()
        header = {'Authorization': token}
        payload = inData
        res = RequestsHandler().post_Req(url, json=payload, headers=header)
        print(res.json())
        return res.json()


if __name__ == '__main__':
    CommonData().creat_CommonData(
        {
            "introduction": "测试测试测试试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测",
            "link": "链接：https://pan.baidu.com/s/1Ao5inos7aVgda4FMoiWcCw?pwd=0wmg 提取码：0wmg 复制这段内容后打开百度网盘手机App，操作更方便哦",
            "official_link": "adsa",
            "platform": "baidu",
            "title": "百度网盘的文件111"

        })
