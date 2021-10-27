# coding:utf-8
import json
import os
import random
import time
from hashlib import md5
import cx_Oracle
import requests

def sql_cha(cursor,my_sql_c):
    try:

        cursor.execute(my_sql_c)
        all_data = cursor.fetchall()
        oo = list(all_data)
        # conn.close()
        return oo
    except cx_Oracle.DatabaseError:
        return print("无效的SQL语句")

def sql_update(setting,v,vv):
    try:
        conns = cx_Oracle.connect(setting[0], setting[1], setting[2])
        cursor = conns.cursor()
        my_sql_c = "UPDATE system_setup SET businessdate = :v,batchdate = :vv".format()
        cursor.execute(my_sql_c, {'v': v,'vv': vv})
        conns.commit()  # 这里一定要commit才行，要不然数据是不会插入的
        conns.close()
        print("核心数据库时间更改成功  {}".format(v))

    except cx_Oracle.DatabaseError:
        return print("无效的SQL语句")
def test_api(url,data):
    try:
        print(f"请求报文：{data}")
        re = requests.post(url, data=json.dumps(data))
        requit = re.json()
        requit["data"] = eval(requit["data"])
        print(f"响应报文：{requit}")
    except:
        requit = re.text
        print(re.text)
        print("接口响应异常")
    return requit







