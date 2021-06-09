import json
import re as res
import time

import requests
from past.builtins import raw_input

import Collect


# os.environ['path'] =  r'E:\instantclient_11_2'
class Hyzllg:
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
            "insuranceNo": "2020082066566007",
            "name": "薛芒乙",
            "idNo": "513436199003021045",
            "idAddress": "浙江省杭州市江干区高教路119号",
            "phone": "16608205407",
            "amount": "5000",
            "periods": "12",
            "purpose": "01",
            "capitalCode": "FBBANK",
            "custGrde": "20.00",
            "email": "ybhdsg@hrtx.com",
            "contactPhone": "17613145209",
            "callbackurl": "callbackurl"
        }

        data["insuranceNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        data["custGrde"] = self.custGrde

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
            "loanReqNo": "20200613910199001",
            "token": "20201124145854137000005034"
        }
        data["loanReqNo"] = self.loanReqNo
        data["token"] = token

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
            "loanReqNo": "2020082066566007",
            "insReqNo": "2020082066566007",
            "name": "薛芒乙",
            "idNo": "513436199003021045",
            "phone": "16608205407",
            "amount": "5000",
            "periods": "12",
            "purpose": "01",
            "premiumRate": "1.417",
            "insurantName": "富邦华一银行",
            "insurantAdd": "上海浦东新区1239号",
            "postCode": "200300",
            "version": "DS_7018_V1.0",
            "docVersion": "V2.0-20200708"
        }
        data["loanReqNo"] = self.loanReqNo
        data["insReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        data["premiumRate"] = premiumRate
        data["insurantName"] = insurantName

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
            "insuranceNo": "2020082066566007",
            "creditReqNo": "2020082088588007",
            "name": "薛芒乙",
            "spelling": "",
            "sex": "00",
            "nationality": "中国",
            "nation": "汉族",
            "birthday": "1985/06/02",
            "idType": "00",
            "loanAmount": 5000,
            "periods": 12,
            "idNo": "513436199003021045",
            "phone": "16608205407",
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
            "profession": "profession",
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
            "bankCard": "6230523610012118577",
            "bankName": "中国农业银行",
            "bankPhone": "17613145209",
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
                "custGrde": "20.00",
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
            "docDate": "2021/01/13"
        }
        data["insuranceNo"] = self.loanReqNo
        data["creditReqNo"] = self.creditReqNo
        data["name"] = self.name
        data["phone"] = self.phone
        data["idNo"] = self.idNo
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankCard
        data["bankName"] = self.bankName
        data["bankPhone"] = self.bankPhone
        data["docDate"] = time.strftime("%Y/%m/%d")
        data["channelDetail"]["custGrde"] = self.custGrde

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
            "creditReqNo": "2020082088588007"
        }
        # data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = self.creditReqNo


        number = 0
        n = False
        while number <= 10:
            url = self.url + 'CREDIT_INQUIRY'
            title = "**********授信结果查询！**********"
            requit = Collect.test_api(url, data, title)
            time.sleep(3)
            if requit["result"] == True:
                print("授信查询接口调用成功！")
                try:
                    if requit["data"]["status"] == "01":
                        print("授信通过！")
                        n = True
                        break
                    elif requit["data"]["status"] == "00":
                        print("授信中！")
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
            "loanReqNo": "202008206656600622",
            "insuranceNo": "",
            "creditReqNo": "202008206656600622"
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


def main(a, hhh):
    abc = []
    for i in range(hhh):
        random__name = Collect.random_name()
        generate__ID = Collect.id_card().generate_ID()
        HB_phone = Collect.phone()
        HB_bankcard = Collect.bankcard()

        # 指定姓名身份证手机号时使用
        # random__name = ""
        # generate__ID = "511123199603083522"
        # HB_phone = ""
        # HB_bankcard = ""

        HB_loanReqNo = Collect.loanReqNo()
        HB_creditReqNo = Collect.creditReqNo()
        # 借款金额
        loanAmount = 5000
        # 期数
        periods = "6"
        # 客户等级上下限
        # custGrde = list(Collect.sql_cha(Collect.hxSIT_ORACLE,"select t.attribute1 from code_library t where t.codeno ='PaiPaiDai'and t.itemno = '{}'".format(periods))[0])[0]
        custGrde = 26.32

        if a == 0:
            hyzllg = Hyzllg(HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,
                            HB_bankcard,
                            "建设银行", HB_phone, Collect.sit_url_pp, custGrde)
            insure = hyzllg.insure_info()  # 投保信息接口
            Insure_Data_Query = hyzllg.insure_data_query(insure)  # 投保资料查询接口
            hyzllg.insure(Insure_Data_Query[0],Insure_Data_Query[1])  # 投保接口
            hyzllg.credit_granting()  # 授信接口
            abc.append([HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone,
                        "5000", periods, HB_bankcard, "建设银行", HB_phone, Collect.sit_url_pp, custGrde])
        elif a == 1:
            hyzllg = Hyzllg(HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,
                            HB_bankcard,
                            "建设银行", HB_phone, Collect.uat_url_pp, custGrde)
            insure = hyzllg.insure_info()  # 投保信息接口
            Insure_Data_Query = hyzllg.insure_data_query(insure)  # 投保资料查询接口
            hyzllg.insure(Insure_Data_Query[0],Insure_Data_Query[1])  # 投保接口
            hyzllg.credit_granting()  # 授信接口
            abc.append([HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone,
                        "5000", periods, HB_bankcard, "建设银行", HB_phone, Collect.uat_url_pp, custGrde])
        elif a == 2:
            hyzllg = Hyzllg(HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,
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
            hyzllg = Hyzllg(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
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


if __name__ == '__main__':
    # 0是SIT
    # 1是UAT
    # 2是DEV
    # main()第一个参数控制测试环境，第二个参数控制数据笔数
    main(0, 1)
