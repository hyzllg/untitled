import cx_Oracle
import json
import os
import time
import re as res

import requests
from past.builtins import raw_input

import Collect


class Hyzllg:
    def __init__(self, loanReqNo, name, idNo, phone, loanAmount, periods, custGrde, bankcard, url, discountRate):
        self.loanReqNo = loanReqNo
        self.name = name
        self.idNo = idNo
        self.phone = phone
        self.loanAmount = loanAmount
        self.periods = periods
        self.bankcard = bankcard
        self.url = url
        self.discountRate = discountRate
        self.custGrde = custGrde

    # def wrapper(func):
    #     def inner(*args, **kwargs):
    #         s = func(*args, **kwargs)
    #         with open(os.path.join(os.path.expanduser("~"), 'Desktop') + "\HUANBEI.log", 'a+',
    #                   encoding='utf-8') as Python_crawler:
    #             Python_crawler.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s[0]} {s[1]} {s[2]}")
    #         return s
    #
    #     return inner

    def insure_info(self):
        data = {
            "channelCustId": "",
            "loanReqNo": self.loanReqNo,
            "capitalCode": "FBBANK",
            "custGrde": self.custGrde,
            "name": self.name,
            "idNo": self.idNo,
            "phone": self.phone,
            "amount": self.loanAmount,
            "periods": self.periods,
            "purpose": "01",
            "addProvince": "110000",
            "addCity": "110000",
            "addDistrict": "110101",
            "addDetail": "学霸路学渣小区1314弄520号",
            "email": "ybhdsg@hrtx.com",
            "contactPhone": "contactPhone",
            "loanRate": 20.00,
            "discountRate": self.discountRate
        }

        # data["loanReqNo"] = self.loanReqNo
        # data["name"] = self.name
        # data["idNo"] = self.idNo
        # data["phone"] = self.phone
        # data["amount"] = self.loanAmount
        # data["periods"] = self.periods
        # data["discountRate"] = self.discountRate
        # data["custGrde"] = self.custGrde

        url = self.url + 'INSURE_INFO'
        title = "**********投保信息接口！**********"
        requit = Collect.test_api(url,data,title)

        if requit["result"] == True:
            print("投保信息接口成功！")
            a = requit["data"]["insurAgencyUrl"]
            b = res.search("lp=(.*)", a)
            c = b.group()[3:]
        else:
            print("投保信息接口失败！")
            raw_input("Press <enter>")

        return c

    def insure_data_query(self, token):
        data = {
            "loanReqNo": self.loanReqNo,
            "token":token

        }
        # data["loanReqNo"] = self.loanReqNo
        # data["token"] = token

        url = self.url + 'INSURE_DATA_QUERY'
        title = "**********投保资料查询接口！**********"
        requit = Collect.test_api(url,data,title)

        if requit["result"] == True:
            print("投保资料查询成功！")
        else:
            print("投保资料查询失败！")
            raw_input("Press <enter>")
        return requit["data"]["premiumRate"]

    def insure(self, a):
        data = {
            "agentNo": "DingSheng",
            "agentName": "鼎盛保险经纪",
            "loanReqNo": self.loanReqNo,
            "insReqNo": self.loanReqNo,
            "name": self.name,
            "idNo": self.idNo,
            "phone": self.phone,
            "amount": self.loanAmount,
            "periods": self.periods,
            "purpose": "01",
            "premiumRate": a,
            "insurantName": "鼎盛",
            "insurantAdd": "上海幸福村521弄1100号",
            "postCode": "110016"
        }
        # data["loanReqNo"] = self.loanReqNo
        # data["insReqNo"] = self.loanReqNo
        # data["name"] = self.name
        # data["idNo"] = self.idNo
        # data["phone"] = self.phone
        # data["amount"] = self.loanAmount
        # data["periods"] = self.periods
        # data["premiumRate"] = a

        url = self.url + 'INSURE'
        title = "**********投保接口！**********"
        requit = Collect.test_api(url,data,title)
        if requit["result"] == True:
            try:
                if requit["data"]["message"]:
                    print("受理失败")
                    raw_input("Press <enter>")
            except BaseException as e:
                if requit["data"]["status"] == '01':
                    print("已受理，处理中！")
        else:
            print("未知异常！")
            raw_input("Press <enter>")
        return requit

    def disburse(self):
        data = {
            "channelCustId": "",
            "loanReqNo": self.loanReqNo,
            "loanRate": 20.00,
            "discountRate": self.discountRate,
            "name": self.name,
            "spelling": "LAIJING",
            "sex": "00",
            "nationality": "中国",
            "nation": "汉族",
            "birthday": "1993/12/12",
            "idType": "00",
            "loanAmount": self.loanAmount,
            "periods": self.periods,
            "phone": self.phone,
            "idNo": self.idNo,
            "idStartDate": "2015/10/08",
            "idEndDate": "2025/10/08",
            "idOffice": "上海市崇明区太上皇路888弄001号",
            "marriage": "00",
            "children": "01",
            "supplyPeople": 0,
            "house": "09",
            "addProvince": "110000",
            "addCity": "110000",
            "addDistrict": "110101",
            "addDetail": "学霸路学渣小区250弄38号",
            "industry": "C",
            "profession": "01",
            "workplaceName": "中国大地保险公司",
            "workTel": "0521-11122844",
            "workProvince": "上海市",
            "workCity": "上海市",
            "workDistrict": "浦东新区",
            "workDetailAdd": "证大五道口1199弄",
            "workAge": 5,
            "income": "02",
            "education": "05",
            "school": "哈弗大学",
            "email": "ybhdsg@hrtx.com",
            "bankCard": self.bankcard,
            "bankName": "建设银行",
            "bankPhone": self.phone,
            "applyProvince": "110000",
            "applyCity": "110000",
            "applyDistrict": "110101",
            "purpose": "01",
            "direction": "04",
            "payType": "00",
            "payMerchantNo": "",
            "authFlag": "01",
            "capitalCode": "FBBANK",
            "agrSignTime": "20200506175500",
            "docDate": "",
            "contacts": [
                {
                    "relation": "01",
                    "name": "鼎盛一",
                    "phoneNo": "17613148801"
                },
                {
                    "relation": "00",
                    "name": "鼎盛二",
                    "phoneNo": "17613148802"
                }
            ],
            "deviceDetail": {
                "deviceId": "646876135467846554646",
                "mac": "NONE",
                "longitude": "162.357159",
                "latitude": "63.589634",
                "gpsCity": "上海市",
                "ip": "192.3.46.57",
                "ipCity": "上海市",
                "oS": "ios"
            },
            "channelDetail": {
                "custGrade": self.custGrde,
                "obtainCustType": "01",
                "faceType": "01",
                "faceScore": 70,
                "verifyResult": "01",
                "fourElementsResult": "01",
                "limitDate": "2020/05/06",
                "limit": 20000.0,
                "balanceLimit": 20000.0,
                "isFirstDisburse": "Y",
                "settleLoanCounts": 1,
                "unclearedLoanCnts": 1,
                "unclearedLoanBaln": 0,
                "overdueD3Days": "N",
                "maxOverdueDays": 14,
                "overdueDays": 4,
                "overdueD3Cnts": 1,
                "isCurrentOverdue": "N",
                "firstRepayOdCnts": 1,
                "beforeLoanSocre": "",
                "midLoanSocre": "",
                "afterLoanSocre": ""
            }
        }
        # data["loanReqNo"] = self.loanReqNo
        # data["name"] = self.name
        # data["phone"] = self.phone
        # data["idNo"] = self.idNo
        # data["loanAmount"] = self.loanAmount
        # data["periods"] = self.periods
        # data["bankCard"] = self.bankcard
        # data["bankPhone"] = self.phone
        # data["discountRate"] = self.discountRate
        # data["channelDetail"]["custGrde"] = self.custGrde

        url = self.url + 'DISBURSE'
        title = "**********支用接口！**********"
        requit = Collect.test_api(url,data,title)


        if requit["result"] == True:
            try:

                if requit["data"]["status"] == "01":
                    print("支用受理成功，处理中！")
                elif requit["data"]["status"] == "00":
                    print("受理失败！")
                    raw_input("Press <enter>")
            except BaseException as e:
                print("未知异常！")
                raw_input("Press <enter>")
        else:
            print("未知异常！")
            raw_input("Press <enter>")


def hb_main(a,b):
    for i in range(b):
        random__name = Collect.random_name()
        generate__ID = Collect.id_card().generate_ID()
        HB_phone = Collect.phone()
        HB_bankcard = Collect.bankcard()
        # 指定姓名身份证手机号时使用
        # random__name = "刘生"
        # generate__ID = "310101199106127639"
        # HB_phone = "13866666666"
        # HB_bankcard = ""
        HB_loanReqNo = Collect.loanReqNo()

        # 借款金额
        loanAmount = 6100
        # 期数
        periods = "6"
        # 客户等级
        custGrde = 18
        # 折后利率

        # discountRate = list(Collect.sql_cha(Collect.hxSIT_ORACLE,
        #                                     "select attribute1 t from code_library t where t.codeno ='HuanbeiArte' and t.itemno = '{}'".format(
        #                                         periods))[0])[0]
        discountRate = 18
        if a == 0:
            hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, HB_bankcard,
                            Collect.sit_url_hb, discountRate)
        elif a == 1:
            hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, HB_bankcard,
                            Collect.uat_url_hb, discountRate)
        elif a == 2:
            hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, HB_bankcard,
                            Collect.dev_url_hb, discountRate)
        else:
            print("........")

        test_info = f'''
                        姓名：{random__name}
                        身份证号：{generate__ID}
                        手机号：{HB_phone}
                        借款金额:{loanAmount}
                        借款期次:{periods}
                        loanReqNo:{HB_loanReqNo}
                    '''
        insure_infos = hyzllg.insure_info()  # 投保信息接口
        Insure_Data_Query = hyzllg.insure_data_query(insure_infos)  # 投保资料查询接口
        hyzllg.insure(Insure_Data_Query)  # 投保接口
        hyzllg.disburse()  # 支用接口
        time.sleep(1)
        print(test_info)
        # raw_input("Press <enter>")


if __name__ == '__main__':
    # 0是SIT
    # 1是UAT
    # 2是DEV
    hb_main(0,1)
