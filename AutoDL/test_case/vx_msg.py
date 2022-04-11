#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/4/8 15:21
# @Author : ZhangTy
# @File : vx_msg.py
import requests


#
# def wx_msg_push():
#     url = 'https://test.autodl.com:33443/api/v1/wechat/message/push'
#     # print(token1)
#     req = {
#         "token": "2b8d64403563",
#         "title": "eg. 来自我的程序",
#         "device": "eg. 我的ImageNet实验",
#         "content": "eg. Epoch=100. Acc=90.2"
#     }
#     r = requests.post(url=url, json=req)
#     print(r.json())


def xianshang_wx_msg_push():
    resp = requests.post("https://www.autodl.com/api/v1/wechat/message/push",
                         json={
                             "token": "a9f0ad8514df",
                             "title": "eg. 来自我的程序",
                             "name": "eg. 我的ImageNet实验",
                             "content": "eg. Epoch=100. Acc=90.2"
                         })

    print(resp.content.decode())


if __name__ == '__main__':
    xianshang_wx_msg_push()
