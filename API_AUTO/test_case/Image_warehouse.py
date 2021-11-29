import os
import sys
import requests
import uuid
import allure
import config.adss
from Auth.auth import AuthManager
from common import Assert, Consts
from common.Logs import Log
from common.Request import RequestsHandler
from common.Return_Response import dict_style

file = os.path.basename(sys.argv[0])
# print(file)
log = Log(file)
logger = log.Logger


@allure.feature("镜像仓库")
@allure.story("公有镜像创建")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase("", "测试用例地址 👇")
@allure.description("正确创建公有镜像")
def test_PublicCreate(img_name=""):
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/public/image/create'

    if img_name == "":
        img_name = uuid.uuid4()
        print("Auto Create a public image by name: ", img_name)
    else:
        print("Create a public image by name: ", img_name)

    data = {
        "image_name": img_name,
        "description": "test_study",
        "is_cache": "false"
    }

    manager = AuthManager(base_url)
    token = manager.showToken()
    # 请求头 授权
    headers = {
        "Authorization": token,
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')
    return img_name.__str__()


@allure.story("公有镜像列表")
def test_PublicList(want_name=""):
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/public/image/list'

    data = {
        "page_index": "1",
        "page_size": "10"
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    # 请求头 授权
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')

    if want_name != "":
        print("Get image id by name: ", want_name)
        array = r.json()["data"]["list"]
        for a in array:
            print(a["public_image_id"])
            print(a["public_image_name"])
            if a["public_image_name"].find(want_name) != -1:
                want_id = a["public_image_id"]
                print("Get id for name: ", want_id)
                return want_id
    else:
        print("Get first cached image id automatically.")
        array = r.json()["data"]["list"]
        for a in array:
            print(a["public_image_id"])
            print(a["public_image_name"])
            print(a["status"])
            if a["status"] == "cache":
                want_id = a["public_image_id"]
                print("Get a cached image: ", want_id)
                return want_id


@allure.story("公有镜像删除缓存")
def test_PublicRemoveCache():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/public/image/remove_cache'
    this_id = test_PublicList()
    print("Will delete this cached image: ", this_id)
    data = {
        "image_id": this_id
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    # 请求头 授权
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')


def PublicDelete(del_id=0):
    base_url = config.adss.server_ip()
    url01 = base_url + "/api/v1/admin/public/image/delete"
    manger = AuthManager(base_url)
    token = manger.showToken()
    headers01 = {
        "Authorization": token
    }
    r = requests.delete(url=url01, json={"image_id": del_id}, headers=headers01)
    print(r.json())


# @allure.story("公有镜像删除")
# def test_PublicDeleteFullSteps():
#     def_name = sys._getframe().f_code.co_name
#     logger.info("开始执行脚本%s:", def_name)
#     name = test_PublicCreate()
#     this_id = test_PublicList(name)
#     print(this_id)
#     PublicDelete(this_id)


@allure.story("创建公有选择缓存镜像")
def test_PublicCreate_Cache():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()

    url = base_url + '/api/v1/admin/public/image/create'

    data = {
        "image_name": "hub.kce.ksyun.com/aivc-kpl/kpl-examples/ray0.8.7-ubuntu18.04-cpu:latest",
        "description": "python_api test_study",
        "is_cache": "true"
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    # 请求头 授权
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')


@allure.story("公有镜像名称校验")
@allure.description("公有镜像不重名是否返回false")
def test_PublicCheckName_False():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/public/image/check_name'

    data = {

        "image_name": "！@#￥%……"
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    # 请求头 授权
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')


@allure.story("公有镜像名称校验")
@allure.description("公有镜像重名是否返回true")
def test_PublicCheckName_True():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/public/image/check_name'

    data = {

        "image_name": "！@#￥%……"
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    # 请求头 授权
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')


@allure.story("公有镜像更新")
@allure.description("正常流程")
def test_PublicUpdate():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/public/image/update'
    name = test_PublicCreate()
    this_id = test_PublicList(name)
    data = {
        "image_id": this_id,
        "image_name": "hub.kce.ksyun.com/aivc-kpl/kpl-examples/ray0.8.7-ubuntu18.04-cpu:latest",
        "description": "test_updata",
        "is_cache": 'false'
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')


@allure.story("公有镜像更新")
@allure.description("更新公有镜像-清除镜像名称进行更新")
def test_PublicUpdate_NotImageName():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/public/image/update'
    name = test_PublicCreate()
    this_id = test_PublicList(name)
    data = {
        "image_id": this_id,
        "image_name": "",
        "description": "test_updata_NotImageName",
        "is_cache": 'false'
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')


@allure.story("公有镜像更新")
@allure.description("更新公有镜像-创建时选择的否，编辑后缓存镜像选择是")
def test_PublicUpdate_CacheYes():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/public/image/update'
    name = test_PublicCreate()
    this_id = test_PublicList(name)
    data = {
        "image_id": this_id,
        "image_name": "hub.kce.ksyun.com/aivc-kpl/kpl-examples/ray0.8.7-ubuntu18.04-cpu:latest",
        "description": "test_updata",
        "is_cache": 'true'
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')


@allure.story("公有镜像更新")
@allure.description("更新公有镜像-创建时选择的是，编辑后缓存镜像选择否")
def test_PublicUpdate_CacheNo():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/public/image/update'
    name = test_PublicCreate()
    this_id = test_PublicList(name)
    data = {
        "image_id": this_id,
        "image_name": "hub.kce.ksyun.com/aivc-kpl/kpl-examples/ray0.8.7-ubuntu18.04-cpu:latest",
        "description": "test_updata",
        "is_cache": 'false'
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')


@allure.story("公有镜像缓存")
def test_PublicStartCache():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/public/image/start_cache'
    name = test_PublicCreate()
    this_id = test_PublicList(name)
    data = {
        "image_id": this_id
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    # 授权
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')


@allure.story("私有镜像列表")
def test_PrivateList():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/private/image/list'

    data = {

        "page_index": "1",
        "page_size": "20"

    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    # 请求头 授权
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')


@allure.story("私有镜像更新")
def test_PrivateUpdate():
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    base_url = config.adss.server_ip()
    url = base_url + '/api/v1/admin/private/image/update'
    # name = test_PublicCreate()
    # this_id = test_PublicList(name)
    data = {
        "image_id": 13,
        "image_name": "private_update test_study",
        "image_tag": "latest",
        "description": "test_study"
    }
    manger = AuthManager(base_url)
    token = manger.showToken()
    # 请求头 授权
    headers = {
        "Authorization": token
    }
    r = RequestsHandler().post_Req(url=url, data=data, headers=headers)
    print(r.json())
    code1 = r.status_code
    str_response = r.content.decode()
    json_response = dict_style(str_response)
    test_assert.assert_code(code1, 200)
    test_assert.assert_body(json_response, 'msg', '')
    Consts.RESULT_LIST.append('pass')



