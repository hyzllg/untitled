import pytest
from page import my_log
import conf
from page.request_func import rd_excle_data
from page.request_func import Oracle_Class
from page.request_func import oracle_conf


# 读取excel用例信息
# @pytest.fixture(scope='class')
# def datas():
#     data = rd_excle_data()
#     return data
@pytest.fixture(scope='session')
def oracle_mate():
    _oracle_conf = oracle_conf(conf.environment)
    hx_oracle = Oracle_Class(_oracle_conf[0][0], _oracle_conf[0][1], _oracle_conf[0][2])
    zw_oracle = Oracle_Class(_oracle_conf[1][0], _oracle_conf[1][1], _oracle_conf[1][2])
    return hx_oracle

# 定义一个全局变量，用于存储内容
global_data = {}
@pytest.fixture()
def set_global_data():
    """
    设置全局变量，用于关联参数
    :return:
    """

    def _set_global_data(key, value):
        global_data[key] = value

    return _set_global_data


@pytest.fixture()
def get_global_data():
    """
    从全局变量global_data中取值
    :return:
    """

    def _get_global_data(key):
        return global_data.get(key)

    return _get_global_data


#日志
@pytest.fixture(scope='function')
def LOG():
    _LOG = my_log.Log()
    return _LOG