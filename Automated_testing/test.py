import cx_Oracle

import Collect



# def sql_update(setting):
#     try:
#         conns = cx_Oracle.connect(setting[0], setting[1], setting[2])
#         cursor = conns.cursor()
#         my_sql_c = f"UPDATE business_apply SET CUSTOMERGROUPLEVEL = :v where customerid = :n"
#         cursor.execute(my_sql_c, {'v': "A1",'n' : "(select customerid from channel_apply_info where creditreqno = '20210513101757681528')"})
#         conns.commit()  # 这里一定要commit才行，要不然数据是不会插入的
#         conns.close()
#
#
#     except cx_Oracle.DatabaseError:
#         return print("无效的SQL语句")

def JH_sql_update(setting):
    try:
        conns = cx_Oracle.connect(setting[0], setting[1], setting[2])
        cursor = conns.cursor()
        my_sql_c = "update business_apply set CUSTOMERGROUPLEVEL = 'B1' where customerid = (select customerid from channel_apply_info where creditreqno = '20210513101757681528')"
        cursor.execute(my_sql_c)
        conns.commit()  # 这里一定要commit才行，要不然数据是不会插入的
        conns.close()
    except cx_Oracle.DatabaseError:
        return print("无效的SQL语句")



environment = Collect.hxSIT_ORACLE


sql = "update business_apply set CUSTOMERGROUPLEVEL = 'B1' where customerid = (select customerid from channel_apply_info where creditreqno = '20210513101757681528')"
sql_update(environment)