"""
全局常量 全部大写
"""
ENV_TEST_IP = 'http://106.38.203.204:30180'
ENV_126_IP = 'http://192.168.1.126:30180'
ENV_185_IP = 'http://192.168.1.185:30180'
ENV_DEV_IP = 'http://106.38.203.204:30190'
ENV_GPU_IP = 'http://106.38.203.204:33000/api/v1/'
ENV_TEST_GPU_IP = 'https://test.autodl.com:33443/api/v1/'
ENV_TEST = "test_study"
ENV_126 = "126"
ENV_185 = "185"
ENV_DEV = "dev"
ENV_DEV_GPU = "dev_gpu"
ENV_TEST_GPU = "test_gpu"


# env 一定要是以上几种，否则默认测试环境
def server_ip(env=ENV_TEST_GPU):
    base_ip = ''
    if env == ENV_TEST:
        base_ip = ENV_TEST_IP
    elif env == ENV_126:
        base_ip = ENV_126_IP
    elif env == ENV_185:
        base_ip = ENV_185_IP
    elif env == ENV_DEV:
        base_ip = ENV_DEV_IP
    elif env == ENV_DEV_GPU:
        base_ip = ENV_GPU_IP
    elif env == ENV_TEST_GPU:
        base_ip = ENV_TEST_GPU_IP

    return base_ip
