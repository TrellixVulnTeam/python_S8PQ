# read_excel.py
import openpyxl


class CasesData:
    """用于保存测试用例数据"""
    pass


class ReadExcel:

    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    def open(self):
        self.wb = openpyxl.load_workbook(self.file_name)
        self.sh = self.wb[self.sheet_name]

    def close(self):
        self.wb.close()

    def read_data(self):
        """按行读取数据，最后返回一个存储字典的列表"""
        self.open()
        rows = list(self.sh.rows)
        titles = []
        for t in rows[0]:
            title = t.value
            titles.append(title)
        cases = []
        for row in rows[1:]:
            case = []
            for r in row:
                case.append(r.value)
            cases.append(dict(zip(titles, case)))
        self.close()
        return cases

    def write_data(self, row, column, msg):
        self.open()
        self.sh.cell(row=row, column=column, value=msg)
        self.wb.save(self.file_name)
        self.close()


if __name__ == '__main__':
    # 直接运行本文件时执行，下面是一个应用实例
    # 需要读取excel时直接调用ReadExcel类   
    test2 = ReadExcel('C:\\Users\\张铁瀛\\PycharmProjects\\api aoto\\test_data\\case.xlsx')
    res2 = test2.read_data()	# 最后返回一个存储字典的列表
    print(res2[0]['case_id'])	# 打印第1个用例的case_id
    print(res2[3]['title'])		# 打印第4个用例的title