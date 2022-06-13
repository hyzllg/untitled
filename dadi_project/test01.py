import os.path
import time
import yaml
from dadi_project.utils import lj_putout_mock, generate_customer_info,api_request,database_manipulation,my_log




def get_oracle_conf(conf,environment):
    oracle_conf = ''
    if environment == "SIT":
        oracle_conf = conf['xxhx_sit_oracle']
    elif environment == "UAT":
        oracle_conf = conf['xsxb_uat_oracle']
    elif environment == "DEV":
        oracle_conf = conf['xsxb_dev_oracle']
    return oracle_conf
environment = 'SIT'
# 获取配置信息
get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
path = os.path.dirname(__file__)
oracle_cf = get_yaml_data(f'{path}/conf/oracle/xxhx_oracle.yaml')
res_url = get_yaml_data(f'{path}/conf/url_res/api_url_tc.yaml')
res_data = get_yaml_data(f'{path}/conf/loan_res/tc_res_data.yaml')
# 日志
log = my_log.Log()
# 获取数据库配置
oracle_conf = get_oracle_conf(oracle_cf, environment)
hx_oracle = database_manipulation.Oracle_Class(oracle_conf[0], oracle_conf[1], oracle_conf[2])
loan = ['PBLG202231171845000509','PBLG202231171845000509']
sql = f"select cooperate,serialno from acct_loan where putoutno in {tuple(loan)}"
print(sql)
data = hx_oracle.query_data(sql)

print(data)




