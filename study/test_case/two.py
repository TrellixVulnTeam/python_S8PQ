import pytest


# class Test2:
# @pytest.mark.parametrize('caseinfo', {'name', 'AAA'}, [{'age', 'BBB'}])
# def test_01_get(self, caseinfo):
#     print("获取Token" + caseinfo)


@pytest.mark.usefixtures('db')
def test_demo(db):
    print("case")
