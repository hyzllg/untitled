import time

import cx_Oracle
import yaml



def datas(number):
    list_datas = []
    for i in range(number):
        tp = (f'40F77C97F04E47DDDF876C9D{str(i+1)}', 'HYZ', f'HYZ{str(i+1)}', '申请', '90', '1', '2021-12-06 12:22:22', 'test666','2021-12-06 12:22:22')
        list_datas.append(tp)
    return list_datas
def insert_data(sql,list_datas,oracle_conf):
    connection = cx_Oracle.connect(oracle_conf[0], oracle_conf[1], oracle_conf[2], encoding="UTF-8",
                                   nencoding="UTF-8")
    cursor = connection.cursor()
    # dataset = [('40F77C97F04E47DDDF876C9D5F1513E1', 'HYZ', 'CPZR005', '申请', '90', '1', '2020-07-07 12:22:22', 'test99', '2020-07-07 12:22:22'),('40F77C97F04E47DDDF876C9D5F1513E2', 'CPZR', 'CPZR005', '申请', '90', '1', '2020-07-07 12:22:22', 'test99', '2020-07-07 12:22:22')]
    cursor.prepare(sql)
    cursor.executemany(None, list_datas)
    connection.commit()
    cursor.close()
    connection.close()
if __name__ == '__main__':
    # 获取配置信息
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    sit_oracle_conf = get_yaml_data('./conf/Config.yaml')["xshx_oracle"]["xsxb_sit_oracle"]
    sql = '''INSERT INTO XBHXBUSI.REFUSE_REASON_LIST (SERIALNO, REFUSEMAINREASON, REFUSESUBREASON, FLOWNO, TERM, ISUSE, UPDATE_DATE, INPUTUSERID, CREATE_DATE) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)'''
    list_datas = datas(60000)
    insert_data(sql,list_datas,sit_oracle_conf)

