import json
import re as res
import time

import cx_Oracle
import requests
from past.builtins import raw_input
import Collect
import easygui


class Hyzllg_360:
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
            "name": self.name,
            "insuranceNo": self.loanReqNo,
            "idNo": self.idNo,
            "idAddress": "上海市浦东新区龙阳路幸福村520号",
            "phone": self.phone,
            "amount": self.loanAmount,
            "periods": self.periods,
            "purpose": "07",
            "capitalCode": self.capitalCode,
            "custGrde": self.custGrde,
            "email": "1264311721@hrtx.com",
            "contactPhone": "18968523600",
            "callbackUrl": "https://www.baidu.com"
        }
        # data["insuranceNo"] = self.loanReqNo
        # data["name"] = self.name
        # data["idNo"] = self.idNo
        # data["phone"] = self.phone
        # data["amount"] = self.loanAmount
        # data["periods"] = self.periods
        # data["custGrde"] = self.custGrde
        # data["capitalCode"] = self.capitalCode

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
        return c,data

    def insure_data_query(self, token):
        data = {
            "loanReqNo": self.loanReqNo,
            "token": token
        }
        # data["loanReqNo"] = self.loanReqNo
        # data["token"] = token

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
            "loanReqNo": self.loanReqNo,
            "insReqNo": self.loanReqNo,
            "name": self.name,
            "idNo": self.idNo,
            "phone": self.phone,
            "amount": self.loanAmount,
            "periods": self.periods,
            "purpose": "07",
            "premiumRate": 1.66,
            "insurantName": "韦艺翠",
            "insurantAdd": "上海市浦东新区龙阳路幸福村520号",
            "postCode": "110016",
            "productId": "7015"
        }
        # data["loanReqNo"] = self.loanReqNo
        # data["insReqNo"] = self.loanReqNo
        # data["name"] = self.name
        # data["idNo"] = self.idNo
        # data["phone"] = self.phone
        # data["amount"] = self.loanAmount
        # data["periods"] = self.periods

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
            "loanReqNo": self.loanReqNo,
            "idNo": self.idNo,
            "insuranceNo": self.loanReqNo,
            "phone": self.phone,
            "loanAmount": self.loanAmount,
            "productId": "7015",
            "name": self.name,
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
            "marriage": "03",
            "education": "06",
            "children": "00",
            "supplyPeople": 0,
            "house": "00",
            "addProvince": "",
            "addCity": "",
            "addDistrict": "",
            "addDetail": "",
            "industry": "C",
            "profession": "18",
            "workplaceName": "大地保险公司",
            "workTel": "13196853698",
            "workProvince": "",
            "workCity": "",
            "workDistrict": "",
            "workDetailAdd": "学院路100号小杨制造厂",
            "workAge": 10,
            "income": "02",
            "school": "清华大学",
            "email": "1264311721@hrtx.com",
            "contacts": [
                {
                    "relation": "00",
                    "name": "哈利路亚",
                    "phoneNo": "18968523600"
                },
            ],
            "bankCard": self.bankcard,
            "bankName": "中国农业银行",
            "bankPhone": "18968523600",
            "applyProvince": "",
            "applyCity": "",
            "applyDistrict": "",
            "periods": self.periods,
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
                "capitalCode": self.capitalCode,
                "custGrde": self.custGrde,
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
        # data["loanReqNo"] = self.loanReqNo
        # data["insuranceNo"] = self.loanReqNo
        # data["name"] = self.name
        # data["phone"] = self.phone
        # data["idNo"] = self.idNo
        # data["loanAmount"] = self.loanAmount
        # data["periods"] = self.periods
        # data["bankCard"] = self.bankcard
        # data["channelDetail"]["custGrde"] = self.custGrde
        # data["channelDetail"]["capitalCode"] = self.capitalCode

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

def main_360(a,b):
    for i in range(b):
        random__name = Collect.random_name()
        generate__ID = Collect.id_card().generate_ID()
        HB_phone = Collect.phone()
        Bank = Collect.bankcard()
        #指定姓名身份证手机号时使用
        # random__name = "殷言"
        # generate__ID = "230602199007074598"
        # HB_phone = "16601065242"
        # Bank = "6214661723533450"

        HB_loanReqNo = Collect.loanReqNo()
        # 借款金额
        loanAmount = 6000
        # 期数
        periods = '6'
        # 客户等级
        custGrde = 27.31
        # 资方代码 (微众：FBBANK，龙江：20062)
        capitalCode = "FBBANK"

        if a == 'sit':
            hyzllg = Hyzllg_360(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, capitalCode,
                            Bank, Collect.sit_url_360)
        elif a == 'uat':
            hyzllg = Hyzllg_360(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, capitalCode,
                            Bank, Collect.uat_url_360)
        elif a == 'dev':
            hyzllg = Hyzllg_360(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, capitalCode,
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
        insure = hyzllg.insure_info()[0]
        hyzllg.insure_data_query(insure)
        hyzllg.insure()
        hyzllg.disburse()
        # Python_crawler.disburse_in_query(test_info)
        time.sleep(1)
        print(test_info)
        # raw_input("Press <enter>")

class Hyzllg_hb:
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

def main_hb(a,b):
    for i in range(b):
        random__name = Collect.random_name()
        generate__ID = Collect.id_card().generate_ID()
        HB_phone = Collect.phone()
        HB_bankcard = Collect.bankcard()
        # 指定姓名身份证手机号时使用
        # random__name = "黄器翠"
        # generate__ID = "450503199503300007"
        # HB_phone = "16605315868"
        # HB_bankcard = ""
        HB_loanReqNo = Collect.loanReqNo()

        # 借款金额
        loanAmount = 6000
        # 期数
        periods = "6"
        # 客户等级
        custGrde = 26.00
        # 折后利率

        # discountRate = list(Collect.sql_cha(Collect.hxSIT_ORACLE,
        #                                     "select attribute1 t from code_library t where t.codeno ='HuanbeiArte' and t.itemno = '{}'".format(
        #                                         periods))[0])[0]
        discountRate = 18
        if a == 'sit':
            hyzllg = Hyzllg_hb(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, HB_bankcard,
                            Collect.sit_url_hb, discountRate)
        elif a == 'uat':
            hyzllg = Hyzllg_hb(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, HB_bankcard,
                            Collect.uat_url_hb, discountRate)
        elif a == 'dev':
            hyzllg = Hyzllg_hb(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, HB_bankcard,
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

class Hyzllg_jh:
    def __init__(self, creditReqNo, loanReqNo, loanReqNo1, name, idNo, phone, loanAmount, periods, bankCard, bankName,
                 bankPhone, url):
        self.creditReqNo = creditReqNo
        self.loanReqNo = loanReqNo
        self.name = name
        self.idNo = idNo
        self.phone = phone
        self.loanAmount = loanAmount
        self.periods = periods
        self.bankCard = bankCard
        self.bankName = bankName
        self.bankPhone = bankPhone
        self.loanReqNo1 = loanReqNo1
        self.url = url

    def wrapper(func):
        def inner(*args, **kwargs):
            s = func(*args, **kwargs)
            with open(os.path.join(os.path.expanduser("~"), 'Desktop') + "\JIAOHANG.log", 'a+',
                      encoding='utf-8') as hyzllg:
                hyzllg.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s[0]} {s[1]} {s[2]}")
            return s

        return inner

    def insure_info(self):
        data = {
            "channelCustId": "",
            "insuranceNo": "2020070152013140002",
            # "creditApplyNo":"",
            "name": "哑巴湖大水怪",
            "idNo": "412721198705203577",
            "phone": "16613145219",
            "idAddress": "落魄山祖师堂",
            "amount": 5000,
            "periods": 3,
            "purpose": "01",
            "laonRate": "8%",
            "insuranceID": "98763",
            "insuranceName": "交行",
            "insuranceAdd": "中国交行",
            "postCode": "110016",
            "stage": "01",
            "callbackUrl": "http://www.woshishui.com"
        }
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        data["insuranceNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods

        a = "**********投保链接接口！**********"
        print(a)
        print(f"请求报文：{data}")
        time.sleep(1)
        re = requests.post(self.url + 'INSURE_INFO', data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            a = requit["data"]["insurUrl"]
            b = res.search("lp=(.*)", a)
            c = b.group()[3:]
            print("投保链接接口成功！")
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")

        return self.url, a, requit, c

    def insure_info_put(self, b):
        url = 'http://10.1.14.106:27405/channel/apitest/BCM/INSURE_INFO'
        data = {
            "channelCustId": "",
            "insuranceNo": "2020070152013140002",
            "creditApplyNo": "20202020202020",
            "name": "哑巴湖大水怪",
            "idNo": "412721198705203577",
            "phone": "16613145219",
            "idAddress": "落魄山祖师堂",
            "amount": 5000,
            "periods": 3,
            "purpose": "01",
            "laonRate": "8%",
            "insuranceID": "98763",
            "insuranceName": "交行",
            "insuranceAdd": "中国交行",
            "postCode": "110016",
            "stage": "02",
            "callbackUrl": "http://www.woshishui.com"
        }
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        data["insuranceNo"] = self.loanReqNo1
        data["creditApplyNo"] = b
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods

        a = "**********投保链接接口！**********"
        print(a)
        print(f"请求报文：{data}")
        time.sleep(1)
        re = requests.post(self.url + 'INSURE_INFO', data=json.dumps(data), headers=headers)
        requit = re.json()

        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            # print(requit)
            a = requit["data"]["insurUrl"]
            b = res.search("lp=(.*)", a)
            c = b.group()[3:]
            print("投保链接接口成功！")
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")

        return self.url, a, requit, c

    def insure_data_query(self, token):
        url = 'http://10.1.14.106:27405/channel/apitest/BCM/INSURE_DATA_QUERY'
        data1 = {
            "loanReqNo": "2020070614351688817",
            "token": ""
        }

        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }

        data1["loanReqNo"] = self.loanReqNo
        data1["token"] = token
        a = "**********投保资料查询接口！**********"
        print(a)
        print(f"请求报文：{data1}")
        time.sleep(1)
        re = requests.post(self.url + 'INSURE_DATA_QUERY', data=json.dumps(data1), headers=headers)
        requit = re.json()

        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            print("投保资料查询成功！")
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")

        return self.url, a, requit

    def insure_data_query_put(self, token):
        url = 'http://10.1.14.106:27405/channel/apitest/BCM/INSURE_DATA_QUERY'
        data1 = {
            "loanReqNo": "2020070614351688817",
            "token": ""
        }

        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }

        data1["loanReqNo"] = self.loanReqNo1
        data1["token"] = token
        a = "**********投保资料查询接口！**********"
        print(a)
        print(f"请求报文：{data1}")
        time.sleep(1)
        re = requests.post(self.url + 'INSURE_DATA_QUERY', data=json.dumps(data1), headers=headers)
        requit = re.json()

        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            print("投保资料查询成功！")
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")

        return self.url, a, requit

    def insure(self):
        url = 'http://10.1.14.106:27405/channel/apitest/BCM/INSURE'
        data = {
            "agentNo": "TianCheng",
            "agentName": "甜橙保代",
            "loanReqNo": "2020070152013140001",
            "insReqNo": "",
            "name": "哑巴湖大水怪",
            "idNo": "412721198705203577",
            "phone": "16613145219",
            "amount": 5000,
            "periods": 3,
            "purpose": "01",
            "premiumRate": 0.08,
            "insurantName": "哑巴湖大水怪",
            "insurantAdd": "被保险人通讯地址",
            "postCode": "110016",
            "stage": "01",
            "version": "",
            "docVersion": ""
        }
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }

        data["loanReqNo"] = self.loanReqNo
        data["insReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        a = "**********投保接口！**********"
        print(a)
        print(f"请求报文：{data}")
        time.sleep(1)
        re = requests.post(self.url + 'INSURE', data=json.dumps(data), headers=headers)
        requit = re.json()

        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            try:
                if requit["data"]["message"]:
                    print("受理失败")
                    print(f'errormsg:{requit["data"]["message"]}')
                    raw_input("Press <enter>")
            except BaseException as e:
                if requit["data"]["status"] == '01':
                    print("已受理，处理中！")
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return self.url, a, requit

    def insure_put(self):
        url = 'http://10.1.14.106:27405/channel/apitest/BCM/INSURE'
        data = {
            "agentNo": "TianCheng",
            "agentName": "甜橙保代",
            "loanReqNo": "2020070152013140001",
            "insReqNo": "",
            "name": "哑巴湖大水怪",
            "idNo": "412721198705203577",
            "phone": "16613145219",
            "amount": 5000,
            "periods": 3,
            "purpose": "01",
            "premiumRate": 0.08,
            "insurantName": "哑巴湖大水怪",
            "insurantAdd": "被保险人通讯地址",
            "postCode": "110016",
            "stage": "02",
            "version": "",
            "docVersion": ""
        }
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }

        data["loanReqNo"] = self.loanReqNo1
        data["insReqNo"] = self.loanReqNo1
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        a = "**********投保接口！**********"
        print(a)
        print(f"请求报文：{data}")
        time.sleep(1)
        re = requests.post(self.url + 'INSURE', data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")

            try:
                if requit["data"]["message"]:
                    print("受理失败")
                    print(f'errormsg:{requit["data"]["message"]}')
                    raw_input("Press <enter>")
            except BaseException as e:
                if requit["data"]["status"] == '01':
                    print("已受理，处理中！")
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return self.url, a, requit

    def credit_granting(self):
        url = 'http://10.1.14.106:27405/channel/apitest/BCM/CREDIT_GRANTING'
        data = {
            "creditReqNo": "20200706456123004",
            "insuranceNo": "2020070616462188640",
            "name": "弘孝琴",
            "idNo": "450222199701040895",
            "phone": "16607067526",
            "spelling": "",
            "loanAmount": 5000,
            "periods": 3,
            "purpose": "01",
            "direction": "00",
            "payType": "00",
            "payMerchantNo": "",
            "authFlag": "01",
            "sex": "00",
            "nationality": "中国",
            "nation": "汉族",
            "birthday": "1990/06/02",
            "idType": "00",
            "idStartDate": "2016/01/18",
            "idEndDate": "2036/01/18",
            "idOffice": "杭州市公安局江干区分局",
            "marriage": "00",
            "children": "01",
            "supplyPeople": 0,
            "house": "05",
            "addProvince": "110000",
            "addCity": "110000",
            "addDistrict": "110101",
            "addDetail": "学霸路学渣小区250弄38号",
            "industry": "C",
            "profession": "00",
            "workplaceName": "大地保险公司",
            "workTel": "021-1254684",
            "workProvince": "",
            "workCity": "",
            "workDistrict": "",
            "workDetailAdd": "学院路100号小杨制造厂",
            "workAge": 5,
            "income": "04",
            "education": "08",
            "school": "哈弗",
            "email": "ybhdsg@hrtx.com",
            "contacts": [
                # {
                #     "relation":"00",
                #     "name":"哑巴湖大水怪",
                #     "phoneNo":"17613145210"
                # },
                # {
                #     "relation":"00",
                #     "name":"哑巴湖大水怪",
                #     "phoneNo":"17613145210"
                # }
            ],
            "bankCard": "6226661203661652",
            "bankName": "招商银行",
            "bankPhone": "13784566444",
            "applyProvince": "110000",
            "applyCity": "110000",
            "applyDistrict": "110101",
            "applyResult": "99",
            "deviceDetail": {
                "deviceId": "",
                "mac": "",
                "longitude": "",
                "latitude": "",
                "gpsCity": "",
                "ip": "",
                "ipCity": "",
                "oS": ""
            },
            "docDate": "",
            "channelDetail": {
                "childProductId": "01",
                "bankLimit": "30000",
                "billAge": "36",
                "insuranceName": "BCM",
                "insuranceAdd": "BCM",
                "postCode": "110016"
            }
        }
        data["creditReqNo"] = self.creditReqNo
        data["insuranceNo"] = self.loanReqNo
        data["name"] = self.name
        data["phone"] = self.phone
        data["idNo"] = self.idNo
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankCard
        data["bankName"] = self.bankName
        data["bankPhone"] = self.bankPhone
        data["docDate"] = time.strftime('%Y/%m/%d')
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********授信接口！**********"
        print(a)
        print(f"请求报文：{data}")
        time.sleep(1)
        re = requests.post(self.url + 'CREDIT_GRANTING', data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            try:

                if requit["data"]["status"] == "01":
                    creditApplyNo = requit["data"]["creditApplyNo"]
                    print("授信受理成功，处理中！")
                elif requit["data"]["status"] == "00":
                    print("受理失败！")
                    if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                        print(f'errormsg:{requit["data"]["errorCode"] + requit["data"]["errorMsg"]}')
                        raw_input("Press <enter>")
            except BaseException as e:
                if requit["data"]["message"]:
                    print(f'error:{requit["data"]["message"]}')


        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return self.url, a, requit, creditApplyNo

    def credit_inquiry(self, creditApplyNo):
        url = 'http://10.1.14.106:27405/channel/apitest/BCM/CREDIT_INQUIRY'
        data = {
            "creditReqNo": "20200706456123001",
            "creditApplyNo": "20200706000000009"
        }
        data["creditReqNo"] = self.creditReqNo
        data["creditApplyNo"] = creditApplyNo
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********授信结果查询接口！**********"
        print(a)
        print(f"请求报文：{data}")
        while True:
            time.sleep(6)
            re = requests.post(self.url + 'CREDIT_INQUIRY', data=json.dumps(data), headers=headers)
            requit = re.json()
            if re.status_code == 200 and requit["result"] == True:
                requit["data"] = eval(requit["data"])
                print(f"响应报文：{requit}")

                try:

                    if requit["data"]["status"] == "01":
                        print("授信通过！")
                        break
                    elif requit["data"]["status"] == "00":
                        print("授信中！")
                        continue
                    else:
                        print("授信失败！")
                        raw_input("Press <enter>")
                except BaseException as e:
                    if requit["data"]["message"]:
                        print(f'error:{requit["data"]["message"]}')


            else:
                print("msg:{}".format(requit["msg"]))
                raw_input("Press <enter>")
        return self.url, a, requit

    def disburse(self, creditApplyNo):
        url = 'http://10.1.14.106:27405/channel/apitest/BCM/DISBURSE'
        data = {
            "loanReqNo": "202007061552308824",
            "creditApplyNo": "20200706000000012",
            "insuranceNo": "202007100000111011",
            "loanAmount": 5000,
            "periods": 3,
            "purpose": "01",
            "currentLimit": "50000",
            "longitude": "",
            "latitude": "",
            "ip": "",
            "contacts": [
                {
                    "relation": "00",
                    "name": "哑巴湖大水怪",
                    "phoneNo": "17613145210"
                },
                {
                    "relation": "00",
                    "name": "哑巴湖大水怪",
                    "phoneNo": "17613145210"
                }
            ],
            "bankCard": "6226661203661652",
            "bankName": "工商银行",
            "bankPhone": "13784566444"
        }
        data["loanReqNo"] = self.loanReqNo1
        data["insuranceNo"] = self.loanReqNo1
        data["creditApplyNo"] = creditApplyNo
        data["phone"] = self.phone
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankCard
        data["bankName"] = self.bankName
        data["bankPhone"] = self.bankPhone
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********提款投保接口！**********"
        print(a)
        print(f"请求报文：{data}")
        time.sleep(1)
        re = requests.post(self.url + 'DISBURSE', data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")

            try:
                if requit["data"]["status"] == '01':
                    print("受理成功，处理中！")
                elif requit["data"]["status"] == '00':
                    print("受理失败！")
                    print(f'Error:{requit["data"]["errorCode"]} {requit["data"]["errorMsg"]}')

            except BaseException as e:
                if requit["data"]["message"]:
                    print("受理失败")
                    print(f'errormsg:{requit["data"]["message"]}')
                    raw_input("Press <enter>")
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return self.url, a, requit

def JH_sql_update(setting,creditreqno):
    try:
        conns = cx_Oracle.connect(setting[0], setting[1], setting[2])
        cursor = conns.cursor()
        my_sql_c = f"update business_apply set CUSTOMERGROUPLEVEL = 'A1' where customerid = (select customerid from channel_apply_info where creditreqno = '{creditreqno}')"
        cursor.execute(my_sql_c)
        conns.commit()  # 这里一定要commit才行，要不然数据是不会插入的
        conns.close()
    except cx_Oracle.DatabaseError:
        return print("无效的SQL语句")

def main_jh(a):
    random__name = Collect.random_name()
    # generate__ID = Collect.id_card().generate_ID()
    JH_phone = Collect.phone()
    JH_bankcard = Collect.bankcard()
    #指定姓名身份证手机号时使用
    # random__name = "'丁名泗"
    generate__ID = "450503199503300007"
    # JH_phone = "16605254115"
    # JH_bankcard = "6214660525152114"

    JH_creditReqNo = Collect.creditReqNo()
    JH_loanReqNo1 = Collect.loanReqNo()
    JH_loanReqNo2 = Collect.loanReqNo()


    # 借款金额
    loanAmount = 13000
    # 期数
    periods = '6'

    if a == 'sit':
        environment = Collect.hxSIT_ORACLE
        hyzllg = Hyzllg_jh(JH_creditReqNo, JH_loanReqNo1, JH_loanReqNo2, random__name, generate__ID, JH_phone, loanAmount,
                        periods,
                        JH_bankcard, "招商银行", JH_phone, Collect.sit_url_jh)
    elif a == 'uat':
        environment = Collect.hxUAT_ORACLE
        hyzllg = Hyzllg_jh(JH_creditReqNo, JH_loanReqNo1, JH_loanReqNo2, random__name, generate__ID, JH_phone, loanAmount,
                        periods,
                        JH_bankcard, "招商银行", JH_phone, Collect.uat_url_jh)
    elif a == 'dev':
        environment = Collect.hxDEV_ORACLE
        hyzllg = Hyzllg_jh(JH_creditReqNo, JH_loanReqNo1, JH_loanReqNo2, random__name, generate__ID, JH_phone, loanAmount,
                        periods,
                        JH_bankcard, "招商银行", JH_phone, Collect.dev_url_jh)
    else:
        print("........")

    test_info = f'''
                    姓名：{random__name}
                    身份证号：{generate__ID}
                    手机号：{JH_phone}
                    借款金额:{loanAmount}
                    借款期次:{periods}
                    creditReqNo:{JH_creditReqNo}
                    loanReqNo:{JH_loanReqNo2}
                '''
    insure = hyzllg.insure_info()
    hyzllg.insure_data_query(insure[-1])
    hyzllg.insure()
    credit_Granting = hyzllg.credit_granting()
    hyzllg.credit_inquiry(credit_Granting[3])
    JH_sql_update(environment,JH_creditReqNo)
    # a = input("aaa")
    insure_put = hyzllg.insure_info_put(credit_Granting[3])
    hyzllg.insure_data_query_put(insure_put[-1])
    hyzllg.insure_put()
    hyzllg.disburse(credit_Granting[3])
    print(test_info)

class Hyzllg_tc:
    def __init__(self, channelCustId, creditReqNo, loanReqNo, name, idNo, phone, loanAmount, periods, bankcard, url,custType):
        self.channelCustId = channelCustId
        self.creditReqNo = creditReqNo
        self.loanReqNo = loanReqNo
        self.name = name
        self.idNo = idNo
        self.phone = phone
        self.loanAmount = loanAmount
        self.periods = periods
        self.bankcard = bankcard
        self.url = url
        self.custType = custType

    # def wrapper(func):
    #     def inner(*args, **kwargs):
    #         s = func(*args, **kwargs)
    #         with open(os.path.join(os.path.expanduser("~"), 'Desktop') + "\ORANGE.log", 'a+',
    #                   encoding='utf-8') as Python_crawler:
    #             Python_crawler.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s[0]} {s[1]} {s[2]}")
    #
    #     return inner

    def credit_granting(self):
        data = {
            "channelCustId": self.channelCustId,
            "creditReqNo": self.creditReqNo,
            "name": self.name,
            "spelling": "ZHANGTIAN",
            "sex": "01",
            "nationality": "中国",
            "nation": "汉族",
            "birthday": "1985/06/02",
            "idType": "00",
            "idNo": self.idNo,
            "idStartDate": "2016/01/18",
            "idEndDate": "2036/01/18",
            "idOffice": "北京市东城区",
            "marriage": "01",
            "children": "00",
            "supplyPeople": 3,
            "house": "00",
            "addProvince": "110000",
            "addCity": "110000",
            "addDistrict": "110101",
            "addDetail": "东大街东大院",
            "industry": "C",
            "profession": "11",
            "workplaceName": "AAA单位",
            "workTel": "13162314539",
            "workProvince": "110000",
            "workCity": "110000",
            "workDistrict": "110101",
            "workDetailAdd": "西大街西大院",
            "workAge": 8,
            "income": "03",
            "education": "06",
            "school": "北京大学",
            "phone": self.phone,
            "email": "email163@qq.com",
            "contacts": [{
                "relation": "00",
                "name": "张三",
                "phoneNo": "15638530000"
            }, {
                "relation": "01",
                "name": "李四",
                "phoneNo": "15638539999"
            }],
            "bankCard": self.bankcard,
            "bankName": "建设银行",
            "bankPhone": self.phone,
            "applyProvince": "110000",
            "applyCity": "110000",
            "applyDistrict": "110101",
            "loanAmount": self.loanAmount,
            "periods": self.periods,
            "purpose": "01",
            "direction": "01",
            "payType": "00",
            "payMerchantNo": "26666",
            "authFlag": "01",
            "deviceDetail": {
                "deviceId": "10-45-5-486",
                "mac": "sjdfsjdfhskldjf ",
                "longitude": "121.551738",
                "latitude": "31.224634",
                "gpsCity": "上海市",
                "ip": "106.14.135.199",
                "ipCity": "上海",
                "os": "android",
                "docDate": "2019/09/12"
            },
            "channelDetail": {
                "citizenshipCheckResult": "1",
                "bankCheckResult": "1",
                "telcoCheckResult": "1",
                "consumeTimes": "1",
                "creditTimes": "1",
                "consumeScene": "1",
                "frontId": "11",
                "reverseId": "11",
                "faceId": "11",
                "woolFlag": "1",
                "phoneFlag": "1",
                "phoneTelco": "1",
                "compScore": "650",
                "repayAbilityScore": "650",
                "comsAmount": "1",
                "finAmount": "1",
                "redPacket": "1",
                "phoneAreaName": "上海市",
                "modelScore": "650",
                "whiteListFlag": "0",
                "sugAmount": "3000.00",
                "sugBasis": "2",
                "loanGrade": "A",
                "registerTime": "1",
                "realNameFlag": "1",
                "realNameGrade": "1",
                "transFlag": "1",
                "custType": self.custType,
                "currLimit": 5000,
                "currRemainLimit": 2000,
                "currLimitOrg": "DD",
                "currLimitStartDate": "2021/05/31",
                "currLimitEndDate": "2021/07/31",
                "currTotalPrice": 28.11,
                "firstLoanFlag": "1",
                "unsettleLoanLimit": 1,
                "settleLoanLimit": 1,
                "lastLoanDate": "2021/04/21",
                "loanAmount": 3000
            }
        }
        # data["channelCustId"] = self.channelCustId
        # data["creditReqNo"] = self.creditReqNo
        # data["name"] = self.name
        # data["idNo"] = self.idNo
        # data["phone"] = self.phone
        # data["loanAmount"] = self.loanAmount
        # data["periods"] = self.periods
        # data["bankCard"] = self.bankcard
        # data["bankPhone"] = self.phone
        # data["channelDetail"]["custType"] = self.custType

        url = self.url + 'CREDIT_GRANTING'
        title = "**********授信申请！**********"
        requit = Collect.test_api(url,data,title)

        if requit["result"] == True:
            creditApplyNo = requit["data"]["body"]["creditApplyNo"]
            print("授信接口调用成功！")
            if requit["data"]["body"]["status"] == "01":
                print("授信受理成功，处理中！")
            else:
                print("授信受理失败！")
                raw_input("Press <enter>")

        else:
            print("未知异常！")
            raw_input("Press <enter>")
        return creditApplyNo

    def credit_inquiry(self, creditApplyNo):
        hhh = 0
        data = {
            "channelCustId": self.channelCustId,
            "creditReqNo": self.creditReqNo,
            "creditApplyNo": creditApplyNo
        }
        # data["channelCustId"] = self.channelCustId
        # data["creditReqNo"] = self.creditReqNo
        # data["creditApplyNo"] = creditApplyNo

        time.sleep(2)
        n = False
        while hhh < 30:
            url = self.url + 'CREDIT_INQUIRY'
            title = "**********授信结果查询！**********"
            requit = Collect.test_api(url, data, title)
            print("授信查询接口调用成功！")
            if requit["data"]["body"]["status"] == "01":
                print("授信通过！")
                n = True
                break
            elif requit["data"]["body"]["status"] == "00":
                print("授信中！")
                time.sleep(3)
                hhh += 1
                continue
            else:
                print("授信失败！")
                raw_input("Press <enter>")


        if hhh >= 16:
            print("甜橙授信时间过长！可能由于授信挡板问题，结束程序！")
            raw_input("Press <enter>")

        return n

    def disburse_trial(self, capitalCode):
        data = {
            "channelCustId": self.channelCustId,
            "periods": self.periods,
            "loanAmount": self.loanAmount
        }
        # data["channelCustId"] = self.channelCustId
        # data["loanAmount"] = self.loanAmount
        # data["periods"] = self.periods

        url = self.url + 'DISBURSE_TRIAL'
        title = "**********支用试算！**********"
        requit = Collect.test_api(url, data, title)
        while True:
            if requit["result"] == True:
                print(f'本次试算资方为：{requit["data"]["body"]["capitalCode"]}')
                if requit["data"]["body"]["status"] == "01" and requit["data"]["body"]["capitalCode"] == capitalCode:
                    print("支用试算成功！")
                    break
                else:
                    time.sleep(3)
                    continue
            else:
                print("未知异常！")
                raw_input("Press <enter>")

    def disburse(self, capitalCode):
        data = {
            "channelCustId": self.channelCustId,
            "loanReqNo": self.loanReqNo,
            "creditReqNo": self.creditReqNo,
            "loanAmount": self.loanAmount,
            "periods": self.periods,
            "purpose": "01",
            "bankCard": self.bankcard,
            "bankCode": "308584000013",
            "bankName": "建设银行",
            "bankPhone": self.phone,
            "longitude": "121.551738",
            "latitude": "31.224634",
            "ip": "192.168.1.2",
            "capitalCode": capitalCode,
            "channelDetail": {
                "woolFlag": "1",
                "phoneFlag": "1",
                "phoneTelco": "1",
                "compScore": "80",
                "repayAbilityScore": "80",
                "comsAmount": "4",
                "finAmount": "2",
                "redPacket": "2",
                "phoneAreaName": "上海市",
                "modelScore": "80",
                "whiteListFlag": "0",
                "loanGrade": "A",
                "registerTime": "2",
                "realNameFlag": "1",
                "realNameGrade": "1",
                "transFlag": "1",
                "custType": self.custType,
                "currLimit": 5000,
                "currRemainLimit": 2000,
                "currLimitOrg": "DD",
                "currLimitStartDate": "2021/05/31",
                "currLimitEndDate": "2021/07/31",
                "currTotalPrice": 28.11,
                "firstLoanFlag": "1",
                "unsettleLoanLimit": 1,
                "settleLoanLimit": 1,
                "lastLoanDate": "2021/04/21",
                "loanAmount": 3000
            }
        }
        # data["channelCustId"] = self.channelCustId
        # data["loanReqNo"] = self.loanReqNo
        # data["creditReqNo"] = self.creditReqNo
        # data["capitalCode"] = capitalCode
        # data["loanAmount"] = self.loanAmount
        # data["periods"] = self.periods
        # data["bankCard"] = self.bankcard
        # data["bankPhone"] = self.phone
        # data["channelDetail"]["custType"] = self.custType

        url = self.url + 'DISBURSE'
        title = "**********支用接口！**********"
        requit = Collect.test_api(url, data, title)
        if requit["result"] == True:
            print("支用接口调用成功！")
            if requit["data"]["body"]["status"] == "01":
                print("受理成功，处理中!")
            else:
                print("受理失败")
                raw_input("Press <enter>")
        else:
            print("未知异常！")
            raw_input("Press <enter>")

    def disburse_in_query(self, loanReqNo):
        data = {
            "channelCustId": self.channelCustId,
            "creditReqNo": loanReqNo,
            "loanReqNo": self.creditReqNo
        }
        data["channelCustId"] = self.channelCustId
        data["loanReqNo"] = loanReqNo
        data["creditReqNo"] = self.creditReqNo

        time.sleep(5)
        while True:
            url = self.url + 'DISBURSE_IN_QUERY'
            title = "**********支用结果查询！**********"
            requit = Collect.test_api(url, data, title)
            if requit["result"] == True:
                print("支用结果查询接口调用成功！")
                if requit["data"]["body"]["status"] == "01":
                    print("支用成功")
                    break
                elif requit["data"]["body"]["status"] == "00":
                    print("处理中！")
                else:
                    print("支用失败！")
                    raw_input("Press <enter>")
            else:
                print("未知异常！")
                raw_input("Press <enter>")
            time.sleep(3)

def main_tc(a, hhh):
    abc = []
    for i in range(hhh):
        random__name = Collect.random_name()
        generate__ID = Collect.id_card().generate_ID()
        ORANGE_phone = Collect.phone()
        ORANGE_bankcard = Collect.bankcard()
        # 指定姓名身份证手机号时使用
        # random__name = "瞿友惠"
        # generate__ID = "360782199412156008"
        # ORANGE_phone = "16607139521"
        # ORANGE_bankcard = ""
        channelCustId = Collect.channelCustId()
        creditReqNo = Collect.creditReqNo()
        loanReqNo = Collect.loanReqNo()
        # 借款金额
        loanAmount = 5000
        # 期数
        periods = "6"
        #客户类型,0是新用户，1是存量活跃，2是存量静默
        custType = "0"
        if a == 'sit':
            hyzllg = Hyzllg_tc(channelCustId, creditReqNo, loanReqNo, random__name, generate__ID, ORANGE_phone,
                            loanAmount, periods, ORANGE_bankcard, Collect.sit_url_tc,custType)
            credit = hyzllg.credit_granting()
            abc.append(
                [channelCustId, creditReqNo, loanReqNo, random__name, generate__ID,
                 ORANGE_phone, loanAmount, periods, ORANGE_bankcard, Collect.sit_url_tc, credit,custType])
        elif a == 'uat':
            hyzllg = Hyzllg_tc(channelCustId, creditReqNo, loanReqNo, random__name, generate__ID, ORANGE_phone,
                            loanAmount, periods, ORANGE_bankcard, Collect.uat_url_tc,custType)
            credit = hyzllg.credit_granting()
            abc.append(
                [channelCustId, creditReqNo, loanReqNo, random__name, generate__ID,
                 ORANGE_phone, loanAmount, periods, ORANGE_bankcard, Collect.uat_url_tc, credit,custType])
        elif a == 'dev':
            hyzllg = Hyzllg_tc(channelCustId, creditReqNo, loanReqNo, random__name, generate__ID, ORANGE_phone,
                            loanAmount, periods, ORANGE_bankcard, Collect.dev_url_tc,custType)
            credit = hyzllg.credit_granting()
            abc.append([channelCustId, creditReqNo, loanReqNo, random__name, generate__ID,
                        ORANGE_phone, loanAmount, periods, ORANGE_bankcard, Collect.dev_url_tc, credit,custType])
        else:
            print("........")

    nnn = False
    n = 0
    # a = input("aaa")
    while len(abc):
        for i in abc:
            hyzllg = Hyzllg_tc(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],i[11])
            if hyzllg.credit_inquiry(i[-1]):
                hyzllg.disburse_trial('FBBANK')
                hyzllg.disburse('FBBANK')
                # Python_crawler.disburse_in_query(ORANGE_serial_number[2])
                abc.remove(i)
                nnn = True
            n += 1
            if n > 30 and nnn == False:
                raw_input("Press <enter>")
            test_info = f'''
                    姓名：{i[3]}
                    身份证号：{i[4]}
                    手机号：{i[5]}
                    借款金额:{i[6]}
                    借款期次:{i[7]}
                    channelCustId：{i[0]}
                    creditReqNo：{i[1]}
                    loanReqNo:{i[2]}
                    '''
            print(test_info)

class Hyzllg_pp:
    def __init__(self, loanReqNo, creditReqNo, name, idNo, phone, loanAmount, periods, bankCard, bankName, bankPhone,
                 url, custGrde):
        self.loanReqNo = loanReqNo
        self.creditReqNo = creditReqNo
        self.name = name
        self.idNo = idNo
        self.phone = phone
        self.loanAmount = loanAmount
        self.periods = periods
        self.bankCard = bankCard
        self.bankName = bankName
        self.bankPhone = bankPhone
        self.url = url
        self.custGrde = custGrde

    def insure_info(self):
        data = {
            "channelCustId": "",
            "insuranceNo": self.loanReqNo,
            "name": self.name,
            "idNo": self.idNo,
            "idAddress": "浙江省杭州市江干区高教路119号",
            "phone": self.phone,
            "amount": self.loanAmount,
            "periods": self.periods,
            "purpose": "01",
            "capitalCode": "FBBANK",
            "custGrde": self.custGrde,
            "email": "ybhdsg@hrtx.com",
            "contactPhone": "17613145209",
            "callbackurl": "callbackurl"
        }

        # data["insuranceNo"] = self.loanReqNo
        # data["name"] = self.name
        # data["idNo"] = self.idNo
        # data["phone"] = self.phone
        # data["amount"] = self.loanAmount
        # data["periods"] = self.periods
        # data["custGrde"] = self.custGrde

        url = self.url + 'INSURE_INFO'
        title = "**********投保信息接口！**********"
        requit = Collect.test_api(url,data,title)


        if requit["result"] == True:
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
            "loanReqNo": self.loanReqNo,
            "token": token
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
        return requit["data"]["insurantName"],requit["data"]["premiumRate"]

    def insure(self, insurantName, premiumRate ):
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
            "premiumRate": premiumRate,
            "insurantName": insurantName,
            "insurantAdd": "上海浦东新区1239号",
            "postCode": "200300",
            "version": "DS_7018_V1.0",
            "docVersion": "V2.0-20200708"
        }
        # data["loanReqNo"] = self.loanReqNo
        # data["insReqNo"] = self.loanReqNo
        # data["name"] = self.name
        # data["idNo"] = self.idNo
        # data["phone"] = self.phone
        # data["amount"] = self.loanAmount
        # data["periods"] = self.periods
        # data["premiumRate"] = premiumRate
        # data["insurantName"] = insurantName

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


    def credit_granting(self):
        data = {
            "channelCustId": "",
            "insuranceNo": self.loanReqNo,
            "creditReqNo": self.creditReqNo,
            "name": self.name,
            "spelling": "",
            "sex": "00",
            "nationality": "中国",
            "nation": "汉族",
            "birthday": "1985/06/02",
            "idType": "00",
            "loanAmount": self.loanAmount,
            "periods": self.periods,
            "idNo": self.idNo,
            "phone": self.phone,
            "idStartDate": "2016/09/04",
            "idEndDate": "2026/09/04",
            "idOffice": "浩然天下宝瓶洲大骊王朝落坡山办祖师堂",
            "idAddress": "浙江省杭州市江干区高教路119号",
            "marriage": "00",
            "children": "",
            "supplyPeople": 0,
            "house": "",
            "addProvince": "",
            "addCity": "",
            "addDistrict": "",
            "addDetail": "",
            "industry": "C",
            "profession": "20",
            "workplaceName": "大地保险公司",
            "workTel": "",
            "workProvince": "",
            "workCity": "",
            "workDistrict": "",
            "workDetailAdd": "",
            "workAge": 0,
            "income": "01",
            "education": "05",
            "school": "",
            "email": "ybhdsg@hrtx.com",
            "contacts": [
                {
                    "relation": "00",
                    "name": "哑巴湖大水怪",
                    "phoneNo": "17613145210"
                },
                {
                    "relation": "00",
                    "name": "哑巴湖大水怪",
                    "phoneNo": "17613145210"
                }
            ],
            "bankCard": self.bankCard,
            "bankName": self.bankName,
            "bankPhone": self.bankPhone,
            "applyProvince": "",
            "applyCity": "",
            "applyDistrict": "",
            "purpose": "01",
            "direction": "",
            "payType": "",
            "payMerchantNo": "",
            "authFlag": "01",
            "deviceDetail": {
                "deviceId": "",
                "mac": "",
                "longitude": "",
                "latitude": "",
                "gpsCity": "",
                "ip": "",
                "ipCity": "",
                "oS": "ios"
            },
            "channelDetail": {
                "capitalCode": "FBBANK",
                "custGrde": self.custGrde,
                "applyEntry": "applyEntry",
                "faceRecoType": "LINKFACE",
                "faceRecoScore": 99,
                "creditDuration": "2020/08/19",
                "currLimit": 50000,
                "currRemainLimit": 50000,
                "firstLoanFlag": "Y",
                "overdueFlag": "N",
                "settleLoanNum": 0,
                "unsettleLoanLimit": 0,
                "unsettleLoanNum": 0,
                "longestOverPeriod": 0,
                "compScore": "1",
                "realFaceCheckResult": "1",
                "citizenshipCheckResult": "1",
                "bankCheckResult": "1",
                "telcoCheckResult": "1"
            },
            "docDate": time.strftime("%Y/%m/%d")
        }
        # data["insuranceNo"] = self.loanReqNo
        # data["creditReqNo"] = self.creditReqNo
        # data["name"] = self.name
        # data["phone"] = self.phone
        # data["idNo"] = self.idNo
        # data["loanAmount"] = self.loanAmount
        # data["periods"] = self.periods
        # data["bankCard"] = self.bankCard
        # data["bankName"] = self.bankName
        # data["bankPhone"] = self.bankPhone
        # data["docDate"] = time.strftime("%Y/%m/%d")
        # data["channelDetail"]["custGrde"] = self.custGrde

        url = self.url + 'CREDIT_GRANTING'
        title = "**********授信接口！**********"
        requit = Collect.test_api(url,data,title)

        if requit["result"] == True:
            try:

                if requit["data"]["status"] == "01":
                    print("授信受理成功，处理中！")
                elif requit["data"]["status"] == "00":
                    print(requit)
                    print("受理失败！")
                    raw_input("Press <enter>")
            except BaseException as e:
                print("未知异常！")
                raw_input("Press <enter>")
        else:
            print("未知异常！")
            raw_input("Press <enter>")

    def credit_inquiry(self):
        data = {
            "channelCustId": "",
            "creditReqNo": self.creditReqNo
        }
        # data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = self.creditReqNo


        number = 0
        n = False
        while number <= 30:
            url = self.url + 'CREDIT_INQUIRY'
            title = "**********授信结果查询！**********"
            requit = Collect.test_api(url, data, title)
            if requit["result"] == True:
                print("授信查询接口调用成功！")
                try:
                    if requit["data"]["status"] == "01":
                        print("授信通过！")
                        n = True
                        break
                    elif requit["data"]["status"] == "00":
                        print("授信中！")
                        time.sleep(3)
                    else:
                        print("授信失败！")
                        raw_input("Press <enter>")
                except BaseException as e:
                    print("未知异常！")
                    raw_input("Press <enter>")

            else:
                print("未知异常！")
                raw_input("Press <enter>")
            number += 1
        if number >= 10:
            print("拍拍贷授信时间过长！可能由于授信挡板问题，结束程序！")
            raw_input("Press <enter>")

        return n

    def disburse(self):
        data = {
            "channelCustId": "",
            "loanReqNo": self.loanReqNo,
            "insuranceNo": "",
            "creditReqNo": self.creditReqNo
        }
        data["creditReqNo"] = self.creditReqNo
        data["loanReqNo"] = self.loanReqNo

        url = self.url + 'DISBURSE'
        title = "**********支用接口！**********"
        requit = Collect.test_api(url, data, title)
        if requit["result"] == True:
            if requit["data"]["status"] == "01":
                print("支用受理成功，处理中！")
            elif requit["data"]["status"] == "00":
                print("支用受理失败！")
                raw_input("Press <enter>")
        else:
            print("未知异常！")
            raw_input("Press <enter>")

    def disburse_in_query(self):
        data = {
            "channelCustId": "",
            "creditReqNo": "132123123",
            "loanReqNo": "202002202002200220"
        }
        data["creditReqNo"] = self.creditReqNo
        data["loanReqNo"] = self.loanReqNo

        while True:
            url = self.url + 'DISBURSE_IN_QUERY'
            title = "**********支用结果查询！**********"
            requit = Collect.test_api(url, data, title)
            if requit["result"] == True:
                print("支用查询接口调用成功！")
                if requit["data"]["status"] == "01":
                    print("支用通过！")
                    break
                elif requit["data"]["status"] == "00":
                    print("支用中！")
                else:
                    print("支用失败！")
                    raw_input("Press <enter>")

            else:
                print("未知异常！")
                raw_input("Press <enter>")

def main_pp(a, hhh):
    abc = []
    for i in range(hhh):
        random__name = Collect.random_name()
        generate__ID = Collect.id_card().generate_ID()
        HB_phone = Collect.phone()
        HB_bankcard = Collect.bankcard()

        # 指定姓名身份证手机号时使用
        # random__name = ""
        # generate__ID = "450503199503300007"
        # HB_phone = ""
        # HB_bankcard = ""

        HB_loanReqNo = Collect.loanReqNo()
        HB_creditReqNo = Collect.creditReqNo()
        # 借款金额
        loanAmount = 6000
        # 期数
        periods = "6"
        # 客户等级上下限
        # custGrde = list(Collect.sql_cha(Collect.hxSIT_ORACLE,"select t.attribute1 from code_library t where t.codeno ='PaiPaiDai'and t.itemno = '{}'".format(periods))[0])[0]
        custGrde = 26.32

        if a == 'sit':
            hyzllg = Hyzllg_pp(HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,
                            HB_bankcard,
                            "建设银行", HB_phone, Collect.sit_url_pp, custGrde)
            insure = hyzllg.insure_info()  # 投保信息接口
            Insure_Data_Query = hyzllg.insure_data_query(insure)  # 投保资料查询接口
            hyzllg.insure(Insure_Data_Query[0],Insure_Data_Query[1])  # 投保接口
            hyzllg.credit_granting()  # 授信接口
            abc.append([HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone,
                        "5000", periods, HB_bankcard, "建设银行", HB_phone, Collect.sit_url_pp, custGrde])
        elif a == 'uat':
            hyzllg = Hyzllg_pp(HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,
                            HB_bankcard,
                            "建设银行", HB_phone, Collect.uat_url_pp, custGrde)
            insure = hyzllg.insure_info()  # 投保信息接口
            Insure_Data_Query = hyzllg.insure_data_query(insure)  # 投保资料查询接口
            hyzllg.insure(Insure_Data_Query[0],Insure_Data_Query[1])  # 投保接口
            hyzllg.credit_granting()  # 授信接口
            abc.append([HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone,
                        "5000", periods, HB_bankcard, "建设银行", HB_phone, Collect.uat_url_pp, custGrde])
        elif a == 'dev':
            hyzllg = Hyzllg_pp(HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,
                            HB_bankcard,
                            "建设银行", HB_phone, Collect.dev_url_pp, custGrde)
            insure = hyzllg.insure_info()  # 投保信息接口
            Insure_Data_Query = hyzllg.insure_data_query(insure)  # 投保资料查询接口
            hyzllg.insure(Insure_Data_Query[0],Insure_Data_Query[1])  # 投保接口
            hyzllg.credit_granting()  # 授信接口
            abc.append([HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone,
                        loanAmount, periods, HB_bankcard, "建设银行", HB_phone, Collect.dev_url_pp, custGrde])
        else:
            print("........")

    time.sleep(5)
    # a = input("aaa")
    nnn = False
    n = 0
    while len(abc):
        for i in abc:
            hyzllg = Hyzllg_pp(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
            if hyzllg.credit_inquiry():
                hyzllg.disburse()
                abc.remove(i)
                nnn = True
            n += 1
            if n > 30 and nnn == False:
                raw_input("Press <enter>")
            test_info = f'''
                            姓名：{i[2]}
                            身份证号：{i[3]}
                            手机号：{i[4]}
                            借款金额:{i[5]}
                            借款期次:{i[6]}
                            loanReqNo:{i[0]}
                            creditReqNo:{i[1]}
                        '''
            print(test_info)

def input_validation():
    while True:
        msg='输入信息'
        title='信息搜集'
        fields=['环境','产品','笔数']
        response=easygui.multenterbox(msg, title, fields, values = ['sit','7014', '1'])
        if response[0].upper() not in ['SIT', 'UAT', 'DEV']:
            easygui.msgbox(msg = "只支持环境\nsit\nuat\ndev", title = '所选环境不支持！',ok_button = '继续选择', image = None, root = None)
            continue
        elif response[1] not in ['7014', '7015', '7016', '7017', '7018']:
            easygui.msgbox(msg = "只支持产品\n7014\n7015\n7016\n7017\n7018", title ='所选产品不支持！', ok_button = '继续选择', image = None, root = None)
            continue
        elif response[2].isdigit() is False:
            easygui.msgbox(msg = "笔数必须是整数", title = 'ERROR', ok_button ='继续选择', image = None, root = None)
            continue        
        break
    return response

def main():
    values = input_validation()
    if values[1] == '7014':
        main_tc(values[0],int(values[2]))
    elif values[1] == '7015':
        main_360(values[0],int(values[2]))
    elif values[1] == '7016':
        main_jh(values[0],int(values[2]))
    elif values[1] == '7017':
        main_hb(values[0],int(values[2]))
    elif values[1] == '7018':
        main_pp(values[0],int(values[2]))


if __name__ == '__main__':
    main()
    raw_input("Press <enter>")

























