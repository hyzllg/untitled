# coding:utf-8
import xlrd
import cProfile
# a = '''{"requestBody":{"applyProvince":"440000","birthday":"1993/11/20","income":"02","channelInfo":{"telcoCheckResult":"0","currRemainLimit":6900.0,"currLimitStartDate":"2021/06/15","whiteListFlag":"0","currLimit":8000.0,"firstLoanFlag":"1","settleLoanLimit":0,"faceId":"group1/M00/02/05/rBHxP1_TCf-AByknAASC6d6SUBo9453264","bankCheckResult":"1","loanAmount":1100.0,"modelScore":"0","lastLoanDate":"2021/06/15","currLimitOrg":"YZF","frontId":"group1/M00/03/03/rBHxPl_TCfGAdxaFAArrZmTRyWc846.jpg","citizenshipCheckResult":"1","custType":"1","phoneAreaName":"湖南省","reverseId":"group1/M00/02/05/rBHxP1_TCfGAYrAqACOivnl5Zz8150.jpg","currLimitEndDate":"2022/06/15","currTotalPrice":"24","compScore":"0","phoneFlag":"2","phoneTelco":"0","unsettleLoanLimit":0},"education":"07","bankCard":"6214834576443646","deviceDetail":{"oS":"android","ip":"180.168.249.244","deviceId":"86a1f45c1b468130","mac":"02:00:00:00:00:00"},"nation":"汉族","creditReqNO":"DADI20210615140514553740512481","workplaceName":"慕容晓晓姐的时候可以","bankName":"招商银行","industry":"M","idNo":"330226199311205110","applyDistrict":"440117","channelDetail":{},"idOffice":"上海市公安局浦东分局","channelCustId":"2020121113562010840466","marriage":"01","channelId":"ORANGE","email":"未知","addProvince":"440000","profession":"18","idType":"00","productId":"7014","idEndDate":"2024/06/19","sex":"01","idStartDate":"2014/06/19","addDistrict":"440117","authFlag":"01","addCity":"440100","bankPhone":"13364691888","addDetail":"上海市虹口区塘沽路463号华虹国际大厦","nationality":"中国","phone":"13364691888","name":"李谦弊","applyCity":"440100","contacts":[{"name":"数据流二","phoneNo":"13303823379","relation":"05"},{"name":"卢总","phoneNo":"15786464948","relation":"04"}]},"requestHead":{"consumerSeqNo":"20210615140515666750","consumerID":"ORANGE"}}'''
# b = '''{"requestBody":{"bankCode":"CMB_D_QB2C","whiteListFlag":"0","bankCard":"6214834576443646","productid":"7014","purpose":"08","ip":"180.168.249.243","creditReqNo":"DADI20210615140514553740512481","bankName":"招商银行","loanReqNo":"2021061514050184388759527","capitalCode":"FBBANK","loanAmount":1100.0,"modelScore":"0","channelDetail":{"currLimitOrg":"YZF","currRemainLimit":6900.0,"currLimitStartDate":"2021/06/15","currLimit":8000.0,"firstLoanFlag":"1","custType":"1","settleLoanLimit":0,"currLimitEndDate":"2022/06/15","currTotalPrice":"24","loanAmount":1100.0,"unsettleLoanLimit":0,"lastLoanDate":"2021/06/15"},"bankPhone":"13364691888","comsAmount":"0","channelCustId":"2020121113562010840466","periods":"6","compScore":"0","phoneFlag":"0","phoneTelco":"0"},"requestHead":{"consumerSeqNo":"20210615141004687467","consumerID":"ORANGE"}}'''
# # 打开文件
# book = xlrd.open_workbook('test.xlsx')
# # 查看所有sheet列表
# print('All sheets: %s' % book.sheet_names())
# null_list = []
# sheet1 = book.sheets()[7]
# print(sheet1.nrows)
# for i in range(sheet1.nrows):
#     row3_values = sheet1.row_values(i)
#     # print(row3_values)2
#     if row3_values[4] == "Y"or"CN":
#         # print(row3_values[1])
#         null_list.append(row3_values[1])
# for i in null_list:
#     if i.strip() not in b:
#         print(i)

from locust import HttpLocust,TaskSet,task

import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})