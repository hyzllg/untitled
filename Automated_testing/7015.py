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


def main_360(environment,number,loanAmount,periods,custGrde,capitalCode):
    for i in range(number):
        HB_loanReqNo = Collect.random_number_reqno()
        random__name = Collect.random_name()
        generate__ID = Collect.id_card().generate_ID()
        HB_phone = Collect.phone()
        Bank = Collect.bankcard()
        #指定姓名身份证手机号时使用
        # random__name = "羊卡国"
        # generate__ID = "220403199512301943"
        # HB_phone = "16608058360"
        # Bank = "6214661723533450"

        # （参数1：apply/query；参数2：流水号；参数3：放款时间，格式y-m-d)
        if capitalCode == "LJBANK":
            loan_datetime = time.strftime("%Y-%m-%d")
            Collect.start_lj_mock()
            ljreqno = Collect.random_number_reqno()
            Collect.update_lj_mock("apply", ljreqno, loan_datetime)
            Collect.update_lj_mock("query", ljreqno, loan_datetime)

        if environment == "SIT":
            hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, capitalCode,
                            Bank, Collect.sit_url_360)
        elif environment == "UAT":
            hyzllg = Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, capitalCode,
                            Bank, Collect.uat_url_360)
        elif environment == "DEV":
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
        insure = hyzllg.insure_info()[0]
        hyzllg.insure_data_query(insure)
        hyzllg.insure()
        hyzllg.disburse()
        # Python_crawler.disburse_in_query(test_info)
        time.sleep(1)
        print(test_info)
        # raw_input("Press <enter>")



def main():
    #环境（sit,uat,dev）
    environment = "sit"
    #走数据笔数
    number = 1
    # 借款金额
    loanAmount = 6000
    # 期数
    periods = '6'
    # 客户等级
    custGrde = 18
    # 资方代码 (微众：FBBANK，龙江：LJBANK)
    capitalCode = "LJBANK"
    main_360(environment.upper(),number,loanAmount,periods,custGrde,capitalCode)

if __name__ == '__main__':
    main()
