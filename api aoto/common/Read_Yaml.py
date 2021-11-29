import yaml
import pprint

from Auth.AutoDL_auth import get_captcha


def get_yaml_data(fileDir):
    reqList = []  # 存放结果[(请求1,响应1),(请求2,期望响应2)]
    # 1- 读取文件操作，从磁盘读取到内存
    fo = open(fileDir, 'r', encoding="utf-8")
    # 2- 使用yaml方法获取数据
    res1 = yaml.load(fo, Loader=yaml.FullLoader)
    fo.close()
    info = res1[0]
    del res1[0]
    for one1 in res1:
        cap_id, cap_val = get_captcha()
        one1['data']['captcha_id'] = cap_id
        one1['data']['captcha_value'] = cap_val
        reqList.append((one1['data'], one1['resp']))

    return reqList  # 存放结果[(请求1,响应1),(请求2,期望响应2)]


if __name__ == '__main__':
    req = get_yaml_data('../test_data/test.yaml')
    # print(res)
    for one in req:
        print(one)
