import pytest


class Test1:

    def test_01(self):
        print("测试1")

    def test_02(self):
        print("测试2")

    def test_03(self, db):
        print("测试3："+str(db))






