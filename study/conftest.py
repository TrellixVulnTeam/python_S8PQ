
# 读取数据的方法
import pytest

#
# def read_yaml():
#     return ['1', '2', '3']
#     # return [{'1', '2', '3'}, {'1', '2', '3'}]


@pytest.fixture(scope="function", autouse=False, name="db")
def exe_sql():
    # print(request.param)
    print("执行sql查询")
    yield
    print("关闭sql")