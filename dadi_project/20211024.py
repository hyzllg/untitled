import yaml
import os
import cx_Oracle
from utils import database_manipulation

data = lambda path : yaml.load(open(path,encoding='utf-8'),Loader=yaml.SafeLoader)
loanNo = '787-503407243301792592'
oracle_driver = data('./conf/Config.yaml')["xshx_oracle"]["xsxb_sit_oracle"]

path = os.path.dirname(__file__)
print(path)
