import os  # 导入os模块


def get_log_path():
    # 1、获取当前文件 test.py 的绝对路径
    # 使用 os 模块当中的path 》abspath （译：abs怕死）的内置变量 __file__获取当前文件的绝对路径
    path1 = os.path.abspath(__file__)

    # 2、dirname （译：的内幕）可以获取当前路径上一级目录所在的绝对路径--B文件夹的绝对路径
    path2 = os.path.dirname(path1)

    # 3、使用 join （译：找in）来拼接 根目录 + B 的绝对路径
    B_DIR = os.path.join(path2, "logs")

    # 4、使用 join 来拼接 C文件名 + aa.py 的绝对路径
    aa_DIR = os.path.join(B_DIR, "log")
    # print(aa_DIR)
    return aa_DIR


def get_login_yaml_path():
    # 1、获取当前文件 test.py 的绝对路径
    # 使用 os 模块当中的path 》abspath （译：abs怕死）的内置变量 __file__获取当前文件的绝对路径
    path1 = os.path.abspath(__file__)

    # 2、dirname （译：的内幕）可以获取当前路径上一级目录所在的绝对路径--B文件夹的绝对路径
    path2 = os.path.dirname(path1)

    # 3、使用 join （译：找in）来拼接 根目录 + B 的绝对路径
    B_DIR = os.path.join(path2, "data")

    # 4、使用 join 来拼接 C文件名 + aa.py 的绝对路径
    aa_DIR = os.path.join(B_DIR, "Login_Data.yaml")
    # print(aa_DIR)
    return aa_DIR


def get_register_yaml_path():
    # 1、获取当前文件 test.py 的绝对路径
    # 使用 os 模块当中的path 》abspath （译：abs怕死）的内置变量 __file__获取当前文件的绝对路径
    path1 = os.path.abspath(__file__)

    # 2、dirname （译：的内幕）可以获取当前路径上一级目录所在的绝对路径--B文件夹的绝对路径
    path2 = os.path.dirname(path1)

    # 3、使用 join （译：找in）来拼接 根目录 + B 的绝对路径
    B_DIR = os.path.join(path2, "data")

    # 4、使用 join 来拼接 C文件名 + aa.py 的绝对路径
    aa_DIR = os.path.join(B_DIR, "Tegister_Data.yaml")
    # print(aa_DIR)
    return aa_DIR


def get_recharge_yaml_path():
    # 1、获取当前文件 test.py 的绝对路径
    # 使用 os 模块当中的path 》abspath （译：abs怕死）的内置变量 __file__获取当前文件的绝对路径
    path1 = os.path.abspath(__file__)

    # 2、dirname （译：的内幕）可以获取当前路径上一级目录所在的绝对路径--B文件夹的绝对路径
    path2 = os.path.dirname(path1)

    # 3、使用 join （译：找in）来拼接 根目录 + B 的绝对路径
    B_DIR = os.path.join(path2, "data")

    # 4、使用 join 来拼接 C文件名 + aa.py 的绝对路径
    aa_DIR = os.path.join(B_DIR, "Recharge_Data.yaml")
    # print(aa_DIR)
    return aa_DIR


def get_instance_yaml_path():
    # 1、获取当前文件 test.py 的绝对路径
    # 使用 os 模块当中的path 》abspath （译：abs怕死）的内置变量 __file__获取当前文件的绝对路径
    path1 = os.path.abspath(__file__)

    # 2、dirname （译：的内幕）可以获取当前路径上一级目录所在的绝对路径--B文件夹的绝对路径
    path2 = os.path.dirname(path1)

    # 3、使用 join （译：找in）来拼接 根目录 + B 的绝对路径
    B_DIR = os.path.join(path2, "data")

    # 4、使用 join 来拼接 C文件名 + aa.py 的绝对路径
    aa_DIR = os.path.join(B_DIR, "Instance_Data.yaml")
    print(aa_DIR)
    return aa_DIR


if __name__ == '__main__':
    get_instance_yaml_path()
