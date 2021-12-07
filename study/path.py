import os


def get_yaml_path():
    path1 = os.path.abspath(__file__)
    path2 = os.path.dirname(path1)
    B_DIR = os.path.join(path2, "test_data")
    A_DIR = os.path.join(B_DIR, "test.yaml")
    print(A_DIR)
    return A_DIR


if __name__ == '__main__':
    get_yaml_path()
