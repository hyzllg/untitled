import yaml
import cx_Oracle
from utils import database_manipulation

data = lambda path : yaml.load(open(path,encoding='utf-8'),Loader=yaml.SafeLoader)
loanNo = '787-503407243301792592'
oracle_driver = data('./conf/Config.yaml')["xshx_oracle"]["xsxb_sit_oracle"]

hx_conn = cx_Oracle.connect(oracle_driver[0], oracle_driver[1], oracle_driver[2])
hx_cursor = hx_conn.cursor()
datas = database_manipulation.DatabaseManipulation().sql_cha(hx_cursor,"select channelcustid from channel_apply_info where creditreqno = (select creditreqno from putout_approve where relativeobjectno = '{}')".format(
                                               loanNo))

# datas = Collect.sql_cha(oracle_driver,"select * from customer_info")


cutomer_info = datas
print(cutomer_info)
