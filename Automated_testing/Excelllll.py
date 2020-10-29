import cx_Oracle

conn = cx_Oracle.connect('xbhxbusi/ccic1234@10.1.12.141:1523/PDEV12UF')  # 用自己的实际数据库用户名、密码、主机ip地址 替换即可
curs = conn.cursor()
sql = 'SELECT * FROM ACCT_PAYMENT_SCHEDULE '  # sql语句
rr = curs.execute(sql)
row = curs.fetchone()
print(row[0])
curs.close()
conn.close()