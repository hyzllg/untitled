import random
import requests
import logging
import json
import time
import re
import os
from logging import handlers

from past.builtins import raw_input

rh = handlers.RotatingFileHandler(os.path.join(os.path.expanduser("~"), 'Desktop') + "\ERROR.log",maxBytes=1024 * 1024 * 5, backupCount=5)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s[line : %(lineno)d] - %(module)s : %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S %p",
    level=logging.ERROR,
    handlers=[rh]
)


class Hyzllg:
    def __init__(self, loanReqNo, name, idNo, phone):
        self.loanReqNo = loanReqNo
        self.name = name
        self.idNo = idNo
        self.phone = phone

    def wrapper(func):
        def inner(*args, **kwargs):
            s = func(*args, **kwargs)
            with open(os.path.join(os.path.expanduser("~"), 'Desktop') + "\360.log", 'a+',
                      encoding='utf-8') as hyzllg:
                hyzllg.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s[0]} {s[1]} {s[2]}\n")

        return inner

    @wrapper
    def insure_info(self):
        url = 'http://10.1.14.106:27405/channel/TEST/QFIN/INSURE_INFO'
        data = {
                 "channelCustId":"",
                 "name":"容邦",
                 "insuranceNo":"2020061845630001",
                 "idNo":"210102199006187178",
                 "idAddress":"上海市浦东新区龙阳路幸福村520号",
                 "phone":"16606185001",
                 "amount":3000.00,
                 "periods":"6",
                 "purpose":"07",
                 "capitalCode":"787",
                 "custGrde":"30",
                 "email":"1264311721@hrtx.com",
                 "contactPhone":"18968523600",
                 "callbackUrl":"https://www.baidu.com"
                }
        data["insuranceNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********投保信息接口！**********"
        print(a)
        time.sleep(3)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            print("投保信息接口调用成功！")
            if requit["data"]["status"]=='01':
                print(requit)
                print("已受理，处理中！")
            else:
                print("受理失败")
                if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                    logging.ERROR(requit["data"]["errorCode"] + "-" + requit["data"]["errorMsg"])
                raw_input("Press <enter>")

        else:
            print("投保信息接口调用异常！")
            raw_input("Press <enter>")
        return url, a, requit

    @wrapper
    def insure_data_query(self):
        url = 'http://10.1.14.106:27405/channel/TEST/QFIN/INSURE_DATA_QUERY'
        data = {
            "loanReqNo": "20200613910199001"
        }
        data["loanReqNo"] = self.loanReqNo
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********投保资料查询接口！**********"
        print(a)
        time.sleep(3)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            print(requit)
            print("投保资料查询成功！")
        else:
            print("投保资料查询接口异常！")
            raw_input("Press <enter>")
        return url, a, requit

    @wrapper
    def insure(self):
        url = 'http://10.1.14.106:27405/channel/TEST/QFIN/INSURE'
        data = {
                "agentNo":"TianCheng",
                "agentName":"甜橙保代",
                "loanReqNo":"20200608002",
                "insReqNo":"20200608002",
                "name":"雷宇蕾",
                "idNo":"513436199106081366",
                "phone":"18717880399",
                "amount":3000.00,
                "periods":"6",
                "purpose":"07",
                "premiumRate":1.66,
                "insurantName":"韦艺翠",
                "insurantAdd":"上海市浦东新区龙阳路幸福村520号",
                "postCode":"110016"
                }
        data["loanReqNo"] = self.loanReqNo
        data["insReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********投保接口！**********"
        print(a)
        time.sleep(3)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:

            print("投保接口调用成功！")
            if requit["data"]["status"] == '01':
                print(requit)
                print("投保成功！")
            else:
                print('投保失败！')
                if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                    logging.ERROR(requit["data"]["errorCode"] + "-" + requit["data"]["errorMsg"])
                raw_input("Press <enter>")
        else:
            print("投保接口调用异常！")
            raw_input("Press <enter>")
        return url, a, requit

    @wrapper
    def disburse(self):
        url = 'http://10.1.14.106:27405/channel/TEST/QFIN/DISBURSE'
        data = {
                 "channelCustId":"",
                 "loanReqNo":"20200608002",
                 "idNo":"513436199106081366",
                "insuranceNo":"20200608002",
                 "phone":"18717880399",
                 "loanAmount":3000.00,
                 "productId":"7015",
                 "name":"雷宇蕾",
                 "spelling":"CHENPI",
                 "sex":"01",
                 "nationality":"中国",
                 "nation":"汉族",
                 "birthday":"1991/01/08",
                 "idType":"00",
                 "idAddress":"上海市浦东新区龙阳路幸福村520号",
                 "idStartDate":"2016/01/18",
                 "idEndDate":"2026/01/18",
                 "idOffice":"杭州市公安局江干区分局",
                 "marriage":"04",
                 "children":"00",
                 "supplyPeople":0,
                 "house":"00",
                 "addProvince":"",
                 "addCity":"",
                 "addDistrict":"",
                 "addDetail":"",
                 "industry":"C",
                 "profession":"12",
                 "workplaceName":"大地保险公司",
                 "workTel":"13196853698",
                 "workProvince":"",
                 "workCity":"",
                 "workDistrict":"",
                 "workDetailAdd":"学院路100号小杨制造厂",
                 "workAge":10,
                 "income":"02",
                 "education":"08",
                 "school":"清华大学",
                 "email":"1264311721@hrtx.com",
                 "contacts":[
                  {
                   "relation":"00",
                   "name":"哈利路亚",
                   "phoneNo":"18968523600"
                  },
                 ],
                 "bankCard":"6230523610012118777",
                 "bankName":"中国农业银行",
                 "bankPhone":"18968523600",
                 "applyProvince":"",
                 "applyCity":"",
                 "applyDistrict":"",
                 "periods":"6",
                 "purpose":"07",
                 "direction":"",
                 "payType":"01",
                 "payMerchantNo":"",
                 "authFlag":"01",
                 "deviceDetail":{
                  "deviceId":"",
                  "mac":"NONE",
                  "longitude":"23.232653",
                  "latitude":"88.369689",
                  "gpsCity":"",
                  "ip":"192.3.46.57",
                  "ipCity":"",
                  "oS":""
                 },
                 "docDate":"",
                 "channelDetail":{
                  "capitalCode":"FBBANK",
                  "custGrde":"30",
                  "payType":"03",
                  "applyEntry":"03",
                  "creditDuration":"2020/03/02",
                  "faceRecoType":"01",
                  "faceRecoScore":66.66,
                  "currLimit":5000.00,
                  "currRemainLimit":5000.00,
                  "firstLoanFlag":"N",
                  "settleLoanNum":1,
                  "unsettleLoanLimit":1,
                  "unsettleLoanNum":1.66,
                  "longestOverPeriod":1,
                  "applyLevel360":100,
                  "actionLevel360":100,
                  "realFaceCheckResult":"1",
                  "citizenshipCheckResult":"1",
                  "bankCheckResult":"1",
                  "telcoCheckResult":"1"
                 }
                }
        data["loanReqNo"] = self.loanReqNo
        data["insuranceNo"] = self.loanReqNo
        data["name"] = self.name
        data["phone"] = self.phone
        data["idNo"] = self.idNo
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用接口！**********"
        print(a)
        time.sleep(3)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            print("支用接口调用成功！")
            if requit["data"]["status"] == "01":
                print(requit)
                print("支用受理成功，处理中！")
            elif requit["data"]["status"] == "00":
                print(requit)
                print("受理失败！")
                if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                    logging.ERROR(requit["data"]["errorCode"] + "-" + requit["data"]["errorMsg"])
                    raw_input("Press <enter>")


        else:
            print("支用接口调用异常！")
            raw_input("Press <enter>")
        return url, a, requit


def loanReqNo():
    a = str(random.randint(1, 1000))
    b = time.strftime("%Y%m%d%H%M%S")
    loanReqNo = b + '88' + a
    return loanReqNo


def phone():
    a = str(random.randint(1000, 10000))
    b = time.strftime("%m%d")
    phone = "166" + b + a
    return phone


def name_idno():
    url = 'http://www.xiaogongju.org/index.php/index/id.html/id/513436/year/1990/month/06/day/14/sex/%E7%94%B7'

    headers = {
        "Content-Type": "text/html;charset=utf-8",
        "Host": "www.xiaogongju.org",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    print("*********爬取姓名身份证信息*********")
    request = requests.get(url, headers=headers)
    ret = request.text
    ret = re.findall('\s<td>\w*</td>', ret)
    new_ret = []
    for i in ret:
        i = i.replace(' ', '')
        i = i.replace('<td>', '')
        i = i.replace('</td>', '')
        new_ret.append(i)
    print(new_ret)
    return new_ret


def main():
    new_name_idno = name_idno()
    HB_loanReqNo = loanReqNo()
    HB_phone = phone()
    hyzllg = Hyzllg(HB_loanReqNo, new_name_idno[0], new_name_idno[1], HB_phone)
    hyzllg.insure_info()
    hyzllg.insure_data_query()
    hyzllg.insure()
    hyzllg.disburse()
    print(
        f'''
        姓名：{new_name_idno[0]}
        身份证号：{new_name_idno[1]}
        手机号：{HB_phone}
        loanReqNo:{HB_loanReqNo}

        '''
    )
    raw_input("Press <enter>")


if __name__ == '__main__':
    main()