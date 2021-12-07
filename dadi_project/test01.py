# -*- coding: utf-8 -*-

"""

性能测试

向Oracle插入 63391 行，耗时 3.03 秒

向Oracle插入 10439134 行，耗时 486.81 秒

"""

import time
import yaml
import cx_Oracle

# 获取配置信息
get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
sit_oracle_conf = get_yaml_data('./conf/Config.yaml')["xshx_oracle"]["xsxb_sit_oracle"]

# 控制每批次插入的数量

batch = 1

connection = cx_Oracle.connect(sit_oracle_conf[0], sit_oracle_conf[1], sit_oracle_conf[2], encoding = "UTF-8", nencoding = "UTF-8")
cursor = connection.cursor()
sql = '''INSERT INTO XBHXBUSI.REFUSE_REASON_LIST (SERIALNO, REFUSEMAINREASON, REFUSESUBREASON, FLOWNO, TERM, ISUSE, UPDATE_DATE, INPUTUSERID, CREATE_DATE) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9);'''
'''
INSERT INTO XBHXBUSI.REFUSE_REASON_LIST (SERIALNO, REFUSEMAINREASON, REFUSESUBREASON, FLOWNO, TERM, ISUSE, UPDATE_DATE, INPUTUSERID, CREATE_DATE) VALUES ('40F77C97F04E47DD8F876C9D5F1513E3', 'CPZR', 'CPZR005', '申请', '90', '1', TO_DATE('2020-07-07 12:22:22', 'YYYY-MM-DD HH24:MI:SS'), 'test99', TO_DATE('2020-07-07 12:22:22', 'YYYY-MM-DD HH24:MI:SS'));
'''
start = time.time()

# 定义需要插入的文本路径

path = u'C:/Users/yepeng/Desktop/Samples/stock_data.txt'

dataset = list()

try:
    with open(path, 'r', encoding='UTF-8') as reader:
        for index, line in enumerate(reader):
            dataset.append(tuple(line.split('|')))
            if (index + 1) % batch == 0:
                cursor.prepare(sql)
                cursor.executemany(None, dataset)
                connection.commit()
                dataset.clear()
                continue

except Exception as e:
    print(e)

finally:

    cursor.executemany(sql, dataset)

    connection.commit()

    dataset.clear()

    cursor.close()

    connection.close()

    elapsed = (time.time() - start)

    print('向Oracle插入 {} 行，耗时 {} 秒'.format(index+1, elapsed))