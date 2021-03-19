import json
import re as res
import time

import requests
from past.builtins import raw_input

import Collect


class Hyzllg:
    def __init__(self, loanReqNo, name, idNo, phone, loanAmount, periods, custGrde ,capitalCode,bankcard,url):
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
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********投保信息接口！**********"
        print(a)
        print(f"请求报文：{data}")
        # time.sleep(1)
        re = requests.post(self.url+'INSURE_INFO', data=json.dumps(data), headers=headers)
        requit = re.json()
        # print(f"响应报文：{requit}")

        if re.status_code == 200 and requit["result"] == True:
            #剥掉两边的引号
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            # print(requit)
            if requit["data"]["status"] == '01':
                a = requit["data"]["insurUrl"]
                b = res.search("lp=(.*)", a)
                c = b.group()[3:]
                print("投保信息接口成功！")
            else:
                print("投保信息接口失败！")
                print(f'errormsg:{requit["data"]["errorCode"] + requit["data"]["errorMsg"]}')
                raw_input("Press <enter>")
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return self.url, a, requit, c

    def insure_data_query(self, token):
        data = {
            "loanReqNo": "20200613910199001",
            "token": ""
        }
        data["loanReqNo"] = self.loanReqNo
        data["token"] = token
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********投保资料查询接口！**********"
        print(a)
        print(f"请求报文：{data}")
        # time.sleep(1)
        re = requests.post(self.url+'INSURE_DATA_QUERY', data=json.dumps(data), headers=headers)
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
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********投保接口！**********"
        print(a)
        print(f"请求报文：{data}")
        # time.sleep(1)
        res = requests.post(self.url+'INSURE', data=json.dumps(data), headers=headers)
        requit = res.json()

        # print(f"响应报文：{requit}")
        if res.status_code == 200 and requit["result"] == True:
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
            "idStartDate": "2016/01/18",
            "idEndDate": "2026/01/18",
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
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用接口！**********"
        print(a)
        print(f"请求报文：{data}")
        # time.sleep(1)
        re = requests.post(self.url+'DISBURSE', data=json.dumps(data), headers=headers)
        requit = re.json()

        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            try:
                if requit["data"]["status"] == "01":
                    print("放款受理成功，处理中！")
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
        return self.url, a, requit

    def disburse_in_query(self, test_info):
        data = {
            "channelCustId": "",
            "loanReqNo": "2020061845630001"
        }
        data["loanReqNo"] = self.loanReqNo
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        while True:

            a = "**********放款结果查询接口！**********"
            print(a)
            print(f"请求报文：{data}")
            time.sleep(10)
            re = requests.post(self.url+'DISBURSE_IN_QUERY', data=json.dumps(data), headers=headers)
            requit = re.json()

            if re.status_code == 200 and requit["result"] == True:
                requit["data"] = eval(requit["data"])
                print(f"响应报文：{requit}")

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
                    if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                        print(f'errormsg:{requit["data"]["errorCode"] + requit["data"]["errorMsg"]}')
                        raw_input("Press <enter>")
                elif requit["data"]["status"] == '02':
                    print("支用失败，银行放款失败")
                    if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                        print(f'errormsg:{requit["data"]["errorCode"] + requit["data"]["errorMsg"]}')
                        raw_input("Press <enter>")
                else:
                    print("未知错误！")
                    raw_input("Press <enter>")

            else:
                print("msg:{}".format(requit["msg"]))
                raw_input("Press <enter>")
            return self.url, a, requit




def main(a):
    random__name = Collect.random_name()
    HB_loanReqNo = Collect.loanReqNo()
    HB_phone = Collect.phone()
    Bank = Collect.bankcard()
    generate__ID = Collect.id_card().generate_ID()
    #借款金额
    loanAmount = 5000
    #期数
    periods = '3'
    #客户等级
    custGrde = 26.00
    #资方代码 (微众：FBBANK，龙江：20062)
    capitalCode = "FBBANK"


    if a == 0:
        hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,custGrde,capitalCode,Bank,Collect.sit_url_360)
        # hyzllg = Hyzllg(HB_loanReqNo, "史燕", "341500199110233057", "16607098581", loanAmount, periods,custGrde,capitalCode,Bank,Collect.sit_url_360)

    elif a == 1:
        hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,custGrde ,capitalCode,Bank, Collect.uat_url_360)
    elif a == 2:
        hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,custGrde ,capitalCode,Bank, Collect.dev_url_360)
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
    hyzllg.insure_data_query(insure[-1])
    hyzllg.insure()
    hyzllg.disburse()
    # hyzllg.disburse_in_query(test_info)
    time.sleep(1)
    print(test_info)
    # raw_input("Press <enter>")


if __name__ == '__main__':
    #0是SIT
    #1是UAT
    #2是DEV
    for i in range(1):
        main(0)