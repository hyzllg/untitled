import json
import os
import time

import requests
from past.builtins import raw_input

import Collect


class Hyzllg:
    def __init__(self, channelCustId, creditReqNo, loanReqNo, name, idNo, phone, loanAmount, periods, bankcard, url):
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

    def wrapper(func):
        def inner(*args, **kwargs):
            s = func(*args, **kwargs)
            with open(os.path.join(os.path.expanduser("~"), 'Desktop') + "\ORANGE.log", 'a+',
                      encoding='utf-8') as hyzllg:
                hyzllg.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s[0]} {s[1]} {s[2]}")

        return inner

    def credit_granting(self):

        url = 'http://10.1.14.106:27405/channel/apitest/TCJQ/CREDIT_GRANTING'
        data = {
            "channelCustId": "20200612886881020",
            "creditReqNo": "20200612668661020",
            "name": "荆宗",
            "spelling": "ZHANGTIAN",
            "sex": "01",
            "nationality": "中国",
            "nation": "汉族",
            "birthday": "1985/06/02",
            "idType": "00",
            "idNo": "51343619900612877X",
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
            "profession": "04",
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
            "phone": "16606124020",
            "email": "email163@qq.com",
            "contacts": [{
                "relation": "00",
                "name": "张三",
                "phoneNo": "15638537485"
            }, {
                "relation": "01",
                "name": "李四",
                "phoneNo": "15638537486"
            }],
            "bankCard": "6214852127765553",
            "bankName": "建设银行",
            "bankPhone": "15638537487",
            "applyProvince": "110000",
            "applyCity": "110000",
            "applyDistrict": "110101",
            "loanAmount": "5000.00",
            "periods": 6,
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
                "transFlag": "1"
            }
        }
        data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = self.creditReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankcard
        data["bankPhone"] = self.phone

        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********授信申请！**********"
        print(a)
        print(f"请求报文：{data}")
        # time.sleep(2)
        re = requests.post(self.url + 'CREDIT_GRANTING', data=json.dumps(data), headers=headers)
        requit = re.json()

        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            creditApplyNo = requit["data"]["body"]["creditApplyNo"]
            print("授信接口调用成功！")
            if requit["data"]["body"]["status"] == "01":
                print("授信受理成功，处理中！")
            else:
                print("授信受理失败！")
                if requit["data"]["message"]:
                    print(f'errormsg:{requit["data"]["message"]}')
                    raw_input("Press <enter>")

        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return self.url, a, requit, creditApplyNo

    def credit_inquiry(self, creditApplyNo):
        hhh = 0
        data = {
            "channelCustId": "20200612886881021",
            "creditReqNo": "20200612668661021",
            "creditApplyNo": ""
        }
        data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = self.creditReqNo
        data["creditApplyNo"] = creditApplyNo
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

        }
        n = False
        while hhh < 8:
            a = "**********授信结果查询！**********"
            print(a)
            print(f"请求报文：{data}")
            time.sleep(1)
            re = requests.post(self.url + 'CREDIT_INQUIRY', data=json.dumps(data), headers=headers)
            requit = re.json()
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            print("授信查询接口调用成功！")
            try:
                if requit["data"]["body"]["status"] == "01":
                    print("授信通过！")
                    n = True
                    break
                elif requit["data"]["body"]["status"] == "00":
                    print("授信中！")
                    hhh += 1
                    continue
                else:
                    print("授信失败！")
                    if requit["data"]["message"]:
                        print(f'errormsg:{requit["data"]["message"]}')
                        raw_input("Press <enter>")
            except BaseException as e:
                print(f'orrer:{requit["data"]["message"]}')
                raw_input("Press <enter>")
        if hhh >= 8:
            print("甜橙授信时间过长！可能由于授信挡板问题，结束程序！")
            raw_input("Press <enter>")

        return self.url, a, requit, n

    def disburse_trial(self, capitalCode):
        url = 'http://10.1.14.106:27405/channel/apitest/TCJQ/DISBURSE_TRIAL'
        data = {
            "channelCustId": "20200612886881021",
            "periods": 6,
            "loanAmount": "1000.00"
        }
        data["channelCustId"] = self.channelCustId
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用试算！**********"
        print(a)
        print(f"请求报文：{data}")
        res = requests.post(self.url + 'DISBURSE_TRIAL', data=json.dumps(data), headers=headers)
        requit = res.json()
        requit["data"] = eval(requit["data"])
        print(f"响应报文：{requit}")
        # time.sleep(1)
        while True:
            if res.status_code == 200 and requit["result"] == True:
                print(f'本次试算资方为：{requit["data"]["body"]["capitalCode"]}')
                if requit["data"]["body"]["status"] == "01" and requit["data"]["body"]["capitalCode"] == capitalCode:
                    print("支用试算成功！")
                    break
                else:
                    time.sleep(3)
                    continue

            else:
                print("msg:{}".format(requit["msg"]))
                raw_input("Press <enter>")
        return self.url, a, requit

    def disburse(self, capitalCode):
        url = 'http://10.1.14.106:27405/channel/apitest/TCJQ/DISBURSE'
        data = {
            "channelCustId": "20200612886881021",
            "loanReqNo": "202006128866881022",
            "creditReqNo": "20200612668661021",
            "loanAmount": "1000.00",
            "periods": 6,
            "purpose": "01",
            "bankCard": "6214852127765553",
            "bankCode": "308584000013",
            "bankName": "建设银行",
            "bankPhone": "13800000004",
            "longitude": "121.551738",
            "latitude": "31.224634",
            "ip": "192.168.1.2",
            "capitalCode": "HNTRUST",
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
                "transFlag": "1"
            }
        }
        data["channelCustId"] = self.channelCustId
        data["loanReqNo"] = self.loanReqNo
        data["creditReqNo"] = self.creditReqNo
        data["capitalCode"] = capitalCode
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankcard
        data["bankPhone"] = self.phone
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用接口！**********"
        print(a)
        print(f"请求报文：{data}")
        time.sleep(1)
        re = requests.post(self.url + 'DISBURSE', data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            print("支用接口调用成功！")
            if requit["data"]["body"]["status"] == "01":
                print("受理成功，处理中!")
            else:
                print("受理失败")
                if requit["data"]["message"]:
                    print(f'errormsg:{requit["data"]["message"]}')
                    raw_input("Press <enter>")
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")

        return self.url, a, requit

    def disburse_in_query(self, loanReqNo):
        url = 'http://10.1.14.106:27405/channel/apitest/TCJQ/DISBURSE_IN_QUERY'
        data = {
            "channelCustId": "20200612886881021",
            "creditReqNo": "20200612668661021",
            "loanReqNo": "202006128866881022"
        }
        data["channelCustId"] = self.channelCustId
        data["loanReqNo"] = loanReqNo
        data["creditReqNo"] = self.creditReqNo
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用结果查询！**********"
        print(a)
        print(f"请求报文：{data}")
        time.sleep(10)
        while True:
            re = requests.post(self.url + 'DISBURSE_IN_QUERY', data=json.dumps(data), headers=headers)
            requit = re.json()
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
            if re.status_code == 200 and requit["result"] == True:
                print("支用结果查询接口调用成功！")
                if requit["data"]["body"]["status"] == "01":
                    print("支用成功")
                    break
                elif requit["data"]["body"]["status"] == "00":
                    print("处理中！")
                else:
                    print("支用失败！")
                    if requit["data"]["message"]:
                        print(f'errormsg:{requit["data"]["message"]}')
                        raw_input("Press <enter>")
            else:
                print("msg:{}".format(requit["msg"]))
                raw_input("Press <enter>")
            time.sleep(10)
        return self.url, a, requit


def main(a, hhh):
    abc = []

    for i in range(hhh):
        random__name = Collect.random_name()
        generate__ID = Collect.id_card().generate_ID()
        ORANGE_phone = Collect.phone()
        ORANGE_bankcard = Collect.bankcard()
        channelCustId = Collect.channelCustId()
        creditReqNo = Collect.creditReqNo()
        loanReqNo = Collect.loanReqNo()
        # 借款金额
        loanAmount = 8000
        # 期数
        periods = "6"
        if a == 0:
            # hyzllg = Hyzllg(channelCustId, creditReqNo,loanReqNo,"滕金炎", "530124199704032387", "16603191127",
            #                 loanAmount, periods, ORANGE_bankcard,Collect.sit_url_tc)
            hyzllg = Hyzllg(channelCustId, creditReqNo, loanReqNo, random__name, generate__ID, ORANGE_phone,
                            loanAmount, periods, ORANGE_bankcard, Collect.sit_url_tc)
            credit = hyzllg.credit_granting()[-1]
            abc.append(
                [channelCustId, creditReqNo, loanReqNo, random__name, generate__ID,
                 ORANGE_phone, loanAmount, periods, ORANGE_bankcard, Collect.sit_url_tc, credit])
        elif a == 1:
            hyzllg = Hyzllg(channelCustId, creditReqNo, loanReqNo, random__name, generate__ID, ORANGE_phone,
                            loanAmount, periods, ORANGE_bankcard, Collect.uat_url_tc)
            credit = hyzllg.credit_granting()[-1]
            abc.append(
                [channelCustId, creditReqNo, loanReqNo, random__name, generate__ID,
                 ORANGE_phone, loanAmount, periods, ORANGE_bankcard, Collect.uat_url_tc, credit])
        elif a == 2:
            hyzllg = Hyzllg(channelCustId, creditReqNo, loanReqNo, random__name, generate__ID, ORANGE_phone,
                            loanAmount, periods, ORANGE_bankcard, Collect.dev_url_tc)
            credit = hyzllg.credit_granting()[-1]
            abc.append([channelCustId, creditReqNo, loanReqNo, random__name, generate__ID,
                        ORANGE_phone, loanAmount, periods, ORANGE_bankcard, Collect.dev_url_tc, credit])
        else:
            print("........")

    time.sleep(5)
    nnn = False
    n = 0
    # a = input("aaa")
    while len(abc):
        for i in abc:
            hyzllg = Hyzllg(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
            if hyzllg.credit_inquiry(i[-1])[-1]:
                hyzllg.disburse_trial('FBBANK')
                hyzllg.disburse('FBBANK')
                # hyzllg.disburse_in_query(ORANGE_serial_number[2])
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


if __name__ == '__main__':
    # 0是SIT
    # 1是UAT
    # 2是DEV
    # main()第一个参数控制测试环境，第二个参数控制数据笔数
    main(0, 1)
