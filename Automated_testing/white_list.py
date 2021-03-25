import Collect

def White(name,idcard,phone,statement,setting):
    try:
        conn = Collect.cx_Oracle.connect(setting[0], setting[1], setting[2])
        cursor = conn.cursor()
        my_sql_c = statement.format(name,idcard,phone)
        cursor.execute(my_sql_c)
        conn.commit()  # 这里一定要commit才行，要不然数据是不会插入的
        conn.close()


    except Collect.cx_Oracle.DatabaseError:
        return print("无效的SQL语句")


if __name__ == '__main__':
    statement = "insert into CUSTOMER_WHITELIST (CUSTOMERNAME, CERTTYPE, CERTID, PHONENO, CREDITLINE, SOURCE, TIME, CREATE_DATE, INPUTUSERID, STATUS, BATCHID, WORKMONTHS, RANK, UPDATE_DATE, FILEDSOURCE)values ('{}', '1', '{}', '{}', 30000.000000, 'A0004', '2099/12/11', to_date('11-12-2020 11:12:39', 'dd-mm-yyyy hh24:mi:ss'), 'test99', '02', '20201211', null, null, to_date('19-10-2020 17:22:57', 'dd-mm-yyyy hh24:mi:ss'), '01')"
    setting = Collect.hxSIT_ORACLE
    random__name = Collect.random_name()
    phone = Collect.phone()
    generate__ID = Collect.id_card().generate_ID()
    White(random__name,generate__ID,phone,statement,setting)
    print(
        f'''
        姓名：{random__name}
        身份证号：{generate__ID}
        手机号：{phone}
        '''


    )