import cx_Oracle

import Collect


def sql_cha(setting,my_sql_c):
    conn = cx_Oracle.connect(setting[0],setting[1],setting[2])
    cursor = conn.cursor()
    cursor.execute(my_sql_c)
    all_data = cursor.fetchall()
    oo = list(all_data)
    return oo

loanNo = "787-502807273301494658"
ACCT_PAYMENT_SCHEDULE = list(sql_cha(Collect.zwSIT_ORACLE,
                                             "select paycorpusamt，actualpaycorpusamt,payinteamt,actualpayinteamt,payfineamt,actualfineamt,paycompdinteamt,actualcompdinteamt,payfeeamt1,actualpayfeeamt1 from ACCT_PAYMENT_SCHEDULE where objectno = '{}'".format(
                                                 loanNo)))

print(ACCT_PAYMENT_SCHEDULE)