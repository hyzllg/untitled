import Collect
import yaml


def White(name, idcard, phone, statement, setting):
    try:
        conn = Collect.cx_Oracle.connect(setting[0], setting[1], setting[2])
        cursor = conn.cursor()
        my_sql_c = statement.format(name, idcard, phone)
        cursor.execute(my_sql_c)
        conn.commit()  # 这里一定要commit才行，要不然数据是不会插入的
        conn.close()


    except Collect.cx_Oracle.DatabaseError:
        return print("无效的SQL语句")


if __name__ == '__main__':
    #获取配置信息
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    res_url = get_yaml_data('../conf/Config.yaml')["xshx_oracle"]
    db_query_all_customer_info = "select customername,certid,phoneno from customer_info where certid in (select distinct A.certid from customer_info A where A.certid not in (select certid from CUSTOMER_WHITELIST))"
    datas = Collect.db_query_all(res_url["xsxb_sit_oracle"], db_query_all_customer_info)
    data = []
    for i in datas:
        if len(i[1]) == 18:
            data = list(i)
            break
        else:
            continue
    statement = "insert into CUSTOMER_WHITELIST (CUSTOMERNAME, CERTTYPE, CERTID, PHONENO, CREDITLINE, SOURCE, TIME, CREATE_DATE, INPUTUSERID, STATUS, BATCHID, WORKMONTHS, RANK, UPDATE_DATE, FILEDSOURCE)values ('{}', '1', '{}', '{}', 30000.000000, 'A0004', '2099/12/11', to_date('11-12-2020 11:12:39', 'dd-mm-yyyy hh24:mi:ss'), 'test99', '02', '20201211', null, null, to_date('19-10-2020 17:22:57', 'dd-mm-yyyy hh24:mi:ss'), '01')"

    White(data[0], data[1], data[2], statement, Collect.res_url["xsxb_sit_oracle"])
    print(
        f'''
        姓名：{data[0]}
        身份证号：{data[1]}
        手机号：{data[2]}
        '''

    )
