# #!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# # -*- coding: utf-8 -*-
# # @Time : 2021/12/23 15:49
# # @Author : ZhangTy
# # @File : test_InstancePowerOffCase.py
# import time
#
# import allure
# import pytest
#
# import config.adss
# from libs.instance_list import *
#
#
# @pytest.mark.last
# class TestInstancePowerOff:
#     @allure.story('实例关机接口')  # 接口名称
#     @allure.title('实例关机用例')  # 用例标题
#     def test_instance_poweroff(self):
#         base_url = config.adss.server_ip()
#         url = base_url + 'instance/power_off'
#         token = change_ticket()
#         header = {'Authorization': token}
#         uuid_list = InstanceList().get_running_InstanceList()
#         print(uuid_list)
#
#         for uid in uuid_list:
#             print(uid)
#             payload = {
#                 "instance_uuid": uid
#             }
#             res = RequestsHandler().post_Req(url, json=payload, headers=header)
#             print(res.json())
#
#         # 500ms * 10 = 5s, timeout=5s
#         all_shutdown = False
#
#         for i in range(10):
#             all_shutdown = InstanceList().is_all_shutdown_InstanceList(uuid_list)
#             if all_shutdown:
#                 break
#             print("waiting...")
#             time.sleep(0.5)
#
#         if all_shutdown:
#             print("succeed")
#         else:
#             print("failed")
#
#     @allure.story('实例释放接口')  # 接口名称
#     @allure.title('实例释放用例')  # 用例标题
#     def test_instance_release(self):
#         base_url = config.adss.server_ip()
#         url = base_url + 'instance/release'
#         token = change_ticket()
#         header = {'Authorization': token}
#         uuid_list = InstanceList().get_shutdown_InstanceList()
#         print(uuid_list)
#
#         for uid in uuid_list:
#             print(uid)
#             payload = {
#                 "instance_uuid": uid
#             }
#             res = RequestsHandler().post_Req(url, json=payload, headers=header)
#             print(res.json())
#
#
# if __name__ == '__main__':
#     pytest.main("-vs", "test_InstancePowerOffCase.py")
