# # 读取数据的方法
# import time
#
# import pytest
#
# import config.adss
# from Auth.AutoDL_auth import change_ticket
# from common.Request import RequestsHandler
# from config.instance_list import InstanceList
#
#
# @pytest.fixture(scope="function", autouse=False, name="clean")
# def test_instance_poweroff():
#
#     yield
#     base_url = config.adss.server_ip()
#     url = base_url + 'instance/power_off'
#     token = change_ticket()
#     header = {'Authorization': token}
#     uuid_list = InstanceList().get_running_InstanceList()
#     print(uuid_list)
#
#     for uid in uuid_list:
#         print(uid)
#         payload = {
#             "instance_uuid": uid
#         }
#         res = RequestsHandler().post_Req(url, json=payload, headers=header)
#         print(res.json())
#
#     # 500ms * 10 = 5s, timeout=5s
#     all_shutdown = False
#
#     for i in range(10):
#         all_shutdown = InstanceList().is_all_shutdown_InstanceList(uuid_list)
#         if all_shutdown:
#             break
#
#         print("waiting...")
#         time.sleep(0.5)
#
#     if all_shutdown:
#         print("succeed")
#     else:
#         print("failed")
#
#
# if __name__ == '__main__':
#     pytest.main("-vs", "test_InstancePowerOffCase.py")
