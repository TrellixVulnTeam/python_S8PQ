import json


# 读取json
def dict_style(data):
    json_response = json.loads(data)
    return json_response
