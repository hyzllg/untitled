#! /usr/bin/python

import cx_Oracle

import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
dsnStr = cx_Oracle.makedsn("127.0.0.1", "1521", "orcl")
conn = cx_Oracle.connect(user="test", password="test", dsn=dsnStr)
c=conn.cursor()
x=c.execute('select * from customer_info')
print (x.fetchone())
c.lose()

conn.close()