import json
import os
import re as res
import time

import cx_Oracle
import requests
from past.builtins import raw_input

import Collect


class Hyzllg:
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

def main(a):
    random__name = Collect.random_name()
    generate__ID = Collect.id_card().generate_ID()
    JH_phone = Collect.phone()
    JH_bankcard = Collect.bankcard()
    #指定姓名身份证手机号时使用
    # random__name = "'丁名泗"
    # generate__ID = "511123199603083522"
    # JH_phone = "16605254115"
    # JH_bankcard = "6214660525152114"

    JH_creditReqNo = Collect.creditReqNo()
    JH_loanReqNo1 = Collect.loanReqNo()
    JH_loanReqNo2 = Collect.loanReqNo()


    # 借款金额
    loanAmount = 13000
    # 期数
    periods = '6'

    if a == 0:
        environment = Collect.hxSIT_ORACLE
        hyzllg = Hyzllg(JH_creditReqNo, JH_loanReqNo1, JH_loanReqNo2, random__name, generate__ID, JH_phone, loanAmount,
                        periods,
                        JH_bankcard, "招商银行", JH_phone, Collect.sit_url_jh)
    elif a == 1:
        environment = Collect.hxUAT_ORACLE
        hyzllg = Hyzllg(JH_creditReqNo, JH_loanReqNo1, JH_loanReqNo2, random__name, generate__ID, JH_phone, loanAmount,
                        periods,
                        JH_bankcard, "招商银行", JH_phone, Collect.uat_url_jh)
    elif a == 2:
        environment = Collect.hxDEV_ORACLE
        hyzllg = Hyzllg(JH_creditReqNo, JH_loanReqNo1, JH_loanReqNo2, random__name, generate__ID, JH_phone, loanAmount,
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


if __name__ == '__main__':
    # 0是SIT
    # 1是UAT
    # 2是DEV
    main(0)
