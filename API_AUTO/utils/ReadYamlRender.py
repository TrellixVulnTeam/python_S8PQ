#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/3/15 18:30
# @Author : ZhangTy
# @File : ReadYamlRender.py
import yaml
import jinja2
from pathlib import Path


class ReadYamlRender:

    def __init__(self, yaml_path, content: dict = {}):
        self._yaml_path = yaml_path
        self._content = content

        with open(FILE_PATH, encoding="utf-8") as w:
            self._string_var = w.read()

    @property
    def render(self):
        response = jinja2.Template(self._string_var).render(self._content)
        results = yaml.safe_load(response)
        return results


if __name__ == '__main__':
    # 测试下封装是否正确
    new_data = {"parent_id": {"name": "被替换的成功的数据-1"}}
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR)
    FILE_PATH = Path.joinpath(BASE_DIR, "data", "LoginCase.yaml")
    print(FILE_PATH)
    print(ReadYamlRender(FILE_PATH, new_data).render)
