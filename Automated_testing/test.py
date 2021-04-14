import yaml
import pytest
import selenium
import requests

import Collect

class file_data():

    def __init__(self,conn,cursor):
        self.conn = conn
        self.cursor = cursor

    def PP_file(self):
        sql = f"select * from loan_batch_info a join (select * from loan_batch_notice where serialno like '20210413%' and repaystatus = '01' and channelrepaysno like '202104132%') b on a.channelrepaysno = b.channelrepaysno"
        datas = f""
        data = Collect.sql_cha(self.conn,sql)

        for i in data:
            a = f"{i[0]}|787-502608163300645072|20290320|00|1|6.0|0.0|5.0|0.0|00|01|00|MA34202009224504|0.00|0.00"



