import json
import re as res
import time

import requests
from past.builtins import raw_input

import Collect


class Hyzllg:
    def __init__(self, loanReqNo, name, idNo, phone, loanAmount, periods, custGrde, capitalCode, bankcard, url):
        self.loanReqNo = loanReqNo
        self.name = name
        self.idNo = idNo
        self.phone = phone
        self.loanAmount = loanAmount
        self.periods = periods
        self.bankcard = bankcard
        self.url = url
        self.custGrde = custGrde
        self.capitalCode = capitalCode

    def insure_info(self):
        data = {
            "channelCustId": "",
            "name": "容邦",
            "insuranceNo": "2020061845630001",
            "idNo": "210102199006187178",
            "idAddress": "上海市浦东新区龙阳路幸福村520号",
            "phone": "16606185001",
            "amount": 1000.00,
            "periods": "6",
            "purpose": "07",
            "capitalCode": "787",
            "custGrde": "18",
            "email": "1264311721@hrtx.com",
            "contactPhone": "18968523600",
            "callbackUrl": "https://www.baidu.com"
        }
        data["insuranceNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        data["custGrde"] = self.custGrde
        data["capitalCode"] = self.capitalCode

        url = self.url + 'INSURE_INFO'
        title = "**********投保信息接口！**********"
        requit = Collect.test_api(url,data,title)
        if requit["data"]["status"] == '01':
            a = requit["data"]["insurUrl"]
            b = res.search("lp=(.*)", a)
            c = b.group()[3:]
            print("投保信息接口成功！")
        else:
            print("投保信息接口失败！")
            raw_input("Press <enter>")
        return c

    def insure_data_query(self, token):
        data = {
            "loanReqNo": "20200613910199001",
            "token": ""
        }
        data["loanReqNo"] = self.loanReqNo
        data["token"] = token

        title = "**********投保资料查询接口！**********"
        url = self.url + 'INSURE_DATA_QUERY'
        requit = Collect.test_api(url,data,title)
        if requit["result"] == True:
            print("投保资料查询成功！")
        else:
            print("投保资料查询失败！")
            raw_input("Press <enter>")

    def insure(self):
        data = {
            "agentNo": "TianCheng",
            "agentName": "甜橙保代",
            "loanReqNo": "20200608002",
            "insReqNo": "20200608002",
            "name": "雷宇蕾",
            "idNo": "513436199106081366",
            "phone": "18717880399",
            "amount": 1000.00,
            "periods": "6",
            "purpose": "07",
            "premiumRate": 1.66,
            "insurantName": "韦艺翠",
            "insurantAdd": "上海市浦东新区龙阳路幸福村520号",
            "postCode": "110016",
            "productId": "7015"
        }
        data["loanReqNo"] = self.loanReqNo
        data["insReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods

        title = "**********投保接口！**********"
        url = self.url + 'INSURE'
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
            print("未知错误！")
            raw_input("Press <enter>")

    def disburse(self):
        data = {
            "channelCustId": "",
            "loanReqNo": "20200608002",
            "idNo": "513436199106081366",
            "insuranceNo": "20200608002",
            "phone": "18717880399",
            "loanAmount": 1000.00,
            "productId": "7015",
            "name": "雷宇蕾",
            "spelling": "CHENPI",
            "sex": "01",
            "nationality": "中国",
            "nation": "汉族",
            "birthday": "1991/01/08",
            "idType": "00",
            "idAddress": "上海市浦东新区龙阳路幸福村520号",
            "idStartDate": "2015/10/08",
            "idEndDate": "2025/10/08",
            "idOffice": "杭州市公安局江干区分局",
            "marriage": "04",
            "children": "00",
            "supplyPeople": 0,
            "house": "00",
            "addProvince": "",
            "addCity": "",
            "addDistrict": "",
            "addDetail": "",
            "industry": "C",
            "profession": "12",
            "workplaceName": "大地保险公司",
            "workTel": "13196853698",
            "workProvince": "",
            "workCity": "",
            "workDistrict": "",
            "workDetailAdd": "学院路100号小杨制造厂",
            "workAge": 10,
            "income": "02",
            "education": "08",
            "school": "清华大学",
            "email": "1264311721@hrtx.com",
            "contacts": [
                {
                    "relation": "00",
                    "name": "哈利路亚",
                    "phoneNo": "18968523600"
                },
            ],
            "bankCard": "6230523610012118777",
            "bankName": "中国农业银行",
            "bankPhone": "18968523600",
            "applyProvince": "",
            "applyCity": "",
            "applyDistrict": "",
            "periods": "6",
            "purpose": "07",
            "direction": "",
            "payType": "01",
            "payMerchantNo": "",
            "authFlag": "01",
            "deviceDetail": {
                "deviceId": "",
                "mac": "NONE",
                "longitude": "23.232653",
                "latitude": "88.369689",
                "gpsCity": "",
                "ip": "192.3.46.57",
                "ipCity": "",
                "oS": ""
            },
            "docDate": "",
            "channelDetail": {
                "capitalCode": "FBBANK",
                "custGrde": "18",
                "payType": "03",
                "applyEntry": "03",
                "creditDuration": "2020/03/02",
                "faceRecoType": "01",
                "faceRecoScore": 66,
                "currLimit": 20000.00,
                "currRemainLimit": 20000.00,
                "firstLoanFlag": "N",
                "settleLoanNum": 1,
                "unsettleLoanLimit": 1,
                "unsettleLoanNum": 1.66,
                "longestOverPeriod": 1,
                "applyLevel360": 100,
                "actionLevel360": 100,
                "realFaceCheckResult": "1",
                "citizenshipCheckResult": "1",
                "bankCheckResult": "1",
                "telcoCheckResult": "1"
            }
        }
        data["loanReqNo"] = self.loanReqNo
        data["insuranceNo"] = self.loanReqNo
        data["name"] = self.name
        data["phone"] = self.phone
        data["idNo"] = self.idNo
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankcard
        data["channelDetail"]["custGrde"] = self.custGrde
        data["channelDetail"]["capitalCode"] = self.capitalCode

        title = "**********支用接口！**********"
        url = self.url + 'DISBURSE'
        requit = Collect.test_api(url,data,title)
        if requit["result"] == True:
            if requit["data"]["status"] == "01":
                print("放款受理成功，处理中！")
            elif requit["data"]["status"] == "00":
                print("受理失败！")
                raw_input("Press <enter>")
        else:
            print("未知错误！")
            raw_input("Press <enter>")

    def disburse_in_query(self, test_info):
        data = {
            "channelCustId": "",
            "loanReqNo": "2020061845630001"
        }
        data["loanReqNo"] = self.loanReqNo
        while True:
            time.sleep(3)
            title = "**********放款结果查询接口！**********"
            url = self.url + 'DISBURSE_IN_QUERY'
            requit = Collect.test_api(url, data, title)

            if requit["result"] == True:
                print("放款结果查询接口调用成功！")
                if requit["data"]["status"] == '01':
                    print("支用成功，银行放款成功！")
                    print(test_info)
                elif requit["data"]["status"] == '00':
                    print("支用中，银行放款中")
                    continue
                elif requit["data"]["status"] == '03':
                    print("授信审批中")
                    continue
                elif requit["data"]["status"] == '04':
                    print("授信审批成功")
                    continue
                elif requit["data"]["status"] == '05':
                    print("授信审批拒绝")
                    raw_input("Press <enter>")
                elif requit["data"]["status"] == '02':
                    print("支用失败，银行放款失败")
                    raw_input("Press <enter>")
                else:
                    print("未知错误！")
                    raw_input("Press <enter>")

            else:
                print("未知错误！")
                raw_input("Press <enter>")


def main(a):
    random__name = Collect.random_name()
    # generate__ID = Collect.id_card().generate_ID()
    HB_phone = Collect.phone()
    Bank = Collect.bankcard()
    #指定姓名身份证手机号时使用
    # random__name = "耿礼荷"
    generate__ID = "511123199603083522"
    # HB_phone = "16605128293"
    # Bank = "6214661723536283"

    HB_loanReqNo = Collect.loanReqNo()
    # 借款金额
    loanAmount = 13000
    # 期数
    periods = '6'
    # 客户等级
    custGrde = 26.00
    # 资方代码 (微众：FBBANK，龙江：20062)
    capitalCode = "FBBANK"

    if a == 0:
        hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, capitalCode,
                        Bank, Collect.sit_url_360)
    elif a == 1:
        hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, capitalCode,
                        Bank, Collect.uat_url_360)
    elif a == 2:
        hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, capitalCode,
                        Bank, Collect.dev_url_360)
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
    insure = hyzllg.insure_info()
    hyzllg.insure_data_query(insure)
    hyzllg.insure()
    hyzllg.disburse()
    # hyzllg.disburse_in_query(test_info)
    time.sleep(1)
    print(test_info)
    # raw_input("Press <enter>")


if __name__ == '__main__':
    # 0是SIT
    # 1是UAT
    # 2是DEV
    for i in range(1):
        main(0)

