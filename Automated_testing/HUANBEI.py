import random
import requests
import logging
import json
import time
import re
import os
from logging import handlers

from past.builtins import raw_input

rh = handlers.RotatingFileHandler(os.path.join(os.path.expanduser("~"), 'Desktop')+"\logging.log",maxBytes=1024*1024*5,backupCount=5)
logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s[line : %(lineno)d] - %(module)s : %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S %p",
    # handlers=[fh,sh],
    level=logging.ERROR,
    handlers=[rh]
)

class Hyzllg:
    def __init__(self,loanReqNo,name,idNo,phone):
        self.loanReqNo = loanReqNo
        self.name = name
        self.idNo = idNo
        self.phone = phone

    def wrapper(func):
        def inner(*args,**kwargs):
            s = func(*args,**kwargs)
            with open(os.path.join(os.path.expanduser("~"), 'Desktop')+"\HUANBEI.log", 'a+', encoding='utf-8') as hyzllg:
                hyzllg.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s[0]} {s[1]} {s[2]}\n")

        return inner

    @wrapper
    def insure_info(self):
        url = 'http://10.1.14.106:27405/channel/TEST/HUANBEI/INSURE_INFO'
        data = {
            "channelCustId":"",
            "loanReqNo":"20200613910199001",
            "capitalCode":"787",
            "custGrde":"GRD36",
            "name":"凤骅",
            "idNo":"513436199006138839",
            "phone":"16606137001",
            "amount":3000.00,
            "periods":6,
            "purpose":"01",
            "addProvince":"110000",
            "addCity":"110000",
            "addDistrict":"110101",
            "addDetail":"学霸路学渣小区250弄38号",
            "email":"ybhdsg@hrtx.com",
            "contactPhone":"17760601111"
        }
        data["loanReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********投保信息接口！**********"
        print(a)
        time.sleep(3)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            print(requit)
            print("投保信息接口成功！")
            if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                logging.ERROR(requit["data"]["errorCode"]+"-"+requit["data"]["errorMsg"])
        else:
            print("投保信息接口异常！")
            raw_input("Press <enter>")
        return url,a,requit

    @wrapper
    def insure_data_query(self):
        url = 'http://10.1.14.106:27405/channel/TEST/HUANBEI/INSURE_DATA_QUERY'
        data = {
            "loanReqNo": "20200613910199001"
        }
        data["loanReqNo"] = self.loanReqNo
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a =  "**********投保资料查询接口！**********"
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
        return url,a,requit

    @wrapper
    def insure(self):
        url = 'http://10.1.14.106:27405/channel/TEST/HUANBEI/INSURE'
        data = {
            "agentNo": "DingSheng",
            "agentName": "鼎盛保险经纪",
            "loanReqNo": "20200613910199001",
            "insReqNo": "20200613910199001",
            "name": "凤骅",
            "idNo": "513436199006138839",
            "phone": "16606137001",
            "amount": 3000.0,
            "periods": 6,
            "purpose": "01",
            "premiumRate": 1.66,
            "insurantName": "鼎盛",
            "insurantAdd": "上海幸福村521弄1100号",
            "postCode": "110016"
        }
        data["loanReqNo"] = self.loanReqNo
        data["insReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********投保接口！**********"
        print(a)
        time.sleep(3)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:

            print("投保接口调用成功！")
            if requit["data"]["status"]=='01':
                print(requit)
                print("投保成功！")
            else:
                print('投保失败！')
                logging.ERROR(requit["data"]["errorMsg"])
                raw_input("Press <enter>")
        else:
            print("投保接口调用异常！")
            raw_input("Press <enter>")
        return url,a,requit

    @wrapper
    def disburse(self):
        url = 'http://10.1.14.106:27405/channel/TEST/HUANBEI/DISBURSE'
        data = {
            "channelCustId": "",
            "loanReqNo": "20200613910199001",
            "name": "凤骅",
            "spelling": "LAIJING",
            "sex": "00",
            "nationality": "中国",
            "nation": "汉族",
            "birthday": "1993/12/12",
            "idType": "00",
            "loanAmount": 3000.0,
            "periods": 6,
            "phone": "16606137001",
            "idNo": "513436199006138839",
            "idStartDate": "2016/01/18",
            "idEndDate": "2026/01/18",
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
            "profession": "02",
            "workplaceName": "中国大地保险公司",
            "workTel": "0521-11122844",
            "workProvince": "上海市",
            "workCity": "上海市",
            "workDistrict": "浦东新区",
            "workDetailAdd": "证大五道口1199弄",
            "workAge": 5,
            "income": "02",
            "education": "08",
            "school": "哈弗大学",
            "email": "ybhdsg@hrtx.com",
            "bankCard": "6214832192941115",
            "bankName": "招商银行",
            "bankPhone": "19888128830",
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
                "custGrade": "GRD36",
                "obtainCustType": "01",
                "faceType": "01",
                "faceScore": 70,
                "verifyResult": "01",
                "fourElementsResult": "01",
                "limitDate": "2020/05/06",
                "limit": 50000.0,
                "balanceLimit": 50000.0,
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
        data["loanReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["phone"] = self.phone
        data["idNo"] = self.idNo
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用接口！**********"
        print(a)
        time.sleep(3)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200 :
            print("支用接口调用成功！")
            if requit["data"]["status"]=="01":
                print(requit)
                print("支用受理成功，处理中！")
            elif requit["data"]["status"]=="00":
                print(requit)
                print("受理失败！")
                if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                    logging.ERROR(requit["data"]["errorCode"]+"-"+requit["data"]["errorMsg"])
                    raw_input("Press <enter>")


        else:
            print("支用接口调用异常！")
            raw_input("Press <enter>")
        return url,a,requit

def loanReqNo():
    a = str(random.randint(1, 1000))
    b = time.strftime("%Y%m%d%H%M%S")
    loanReqNo = b + '88' + a
    return loanReqNo



def phone():
    a = str(random.randint(1000,10000))
    b = time.strftime("%m%d")
    phone = "166"+b+a
    return phone


def name_idno():
    url = 'http://www.xiaogongju.org/index.php/index/id.html/id/513436/year/1990/month/06/day/14/sex/%E7%94%B7'

    headers = {
        "Content-Type":"text/html;charset=utf-8",
        "Host":"www.xiaogongju.org",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    print("*********爬取姓名身份证信息*********")
    request = requests.get(url,headers=headers)
    ret = request.text
    ret = re.findall('\s<td>\w*</td>',ret)
    new_ret = []
    for i in ret:
        i = i.replace(' ','')
        i = i.replace('<td>','')
        i = i.replace('</td>','')
        new_ret.append(i)
    print(new_ret)
    return new_ret

def main():
    new_name_idno = name_idno()
    HB_loanReqNo = loanReqNo()
    HB_phone = phone()
    hyzllg = Hyzllg(HB_loanReqNo,new_name_idno[0],new_name_idno[1],HB_phone)
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