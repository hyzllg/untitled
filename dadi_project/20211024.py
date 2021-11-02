import yaml
import os
import cx_Oracle
from utils import database_manipulation

data = lambda path : yaml.load(open(path,encoding='utf-8'),Loader=yaml.SafeLoader)
loanNo = '787-503407243301792592'
oracle_conf = data('./conf/Config.yaml')["xshx_oracle"]["xsxb_sit_oracle"]

#创建数据库连接

conn = cx_Oracle.connect(oracle_conf[0],oracle_conf[1],oracle_conf[2])

#创建cursor

cursor = conn.cursor()

#执行sql

sql1 = "select A.COLUMN_NAME,A.DATA_TYPE  from user_tab_columns A where TABLE_NAME='CUSTOMER_INFO'"
sql2 = "select * from customer_info where customerid = '320000000651293'"

cursor.execute(sql1)
data1 = cursor.fetchall()
print(data1[0][0])
cursor.execute(sql2)
data2 = cursor.fetchall()
print(data2)
dict1 = {}
for i,v in enumerate(data1):
    dict1[v[0]] = data2[0][i]
print(dict1)

conn.close()


