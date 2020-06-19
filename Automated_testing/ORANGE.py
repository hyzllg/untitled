import random
import logging
import requests
import json
import time
import re
import os
from logging import handlers
from past.builtins import raw_input

rh = handlers.RotatingFileHandler(os.path.join(os.path.expanduser("~"), 'Desktop')+"\ERROR.log",maxBytes=1024*1024*5,backupCount=5)
#os.path.expanduser("~"), 'Desktop' 获取电脑桌面路径
logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s[line : %(lineno)d] - %(module)s : %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S %p",
    # handlers=[fh,sh],
    level=logging.ERROR,
    handlers=[rh]
)



class Hyzllg:
    def __init__(self,channelCustId,creditReqNo,name,idNo,phone):
        self.channelCustId = channelCustId
        self.creditReqNo = creditReqNo
        self.name = name
        self.idNo = idNo
        self.phone = phone

    def wrapper(func):
        def inner(*args,**kwargs):
            s = func(*args,**kwargs)
            with open(os.path.join(os.path.expanduser("~"), 'Desktop')+"\ORANGE.log", 'a+', encoding='utf-8') as hyzllg:
                hyzllg.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s[0]} {s[1]} {s[2]}\n")

        return inner
    @wrapper
    def credit_granting(self):

        url = 'http://10.1.14.106:27405/channel/TEST/TCJQ/CREDIT_GRANTING'
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
            "email":"email163@qq.com",
            "contacts": [{
                "relation": "00",
                "name": "张三",
                "phoneNo": "15638537485"
            },{
                "relation": "01",
                "name": "李四",
                "phoneNo": "15638537486"
             }],
            "bankCard": "6230523610012118577",
            "bankName": "中国农业银行",
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
                    "citizenshipCheckResult":"1",
                    "bankCheckResult":"1",
                    "telcoCheckResult":"1",
                    "consumeTimes":"1",
                    "creditTimes":"1",
                    "consumeScene":"1",
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

        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********授信申请！**********"
        print(a)
        time.sleep(3)
        re = requests.post(url,data=json.dumps(data),headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            print("授信接口调用成功！")
            if requit["data"]["status"] == "01":
                print(requit)
                print("授信受理成功，处理中！")
            else:
                print("授信受理失败！")
                if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                    logging.ERROR(requit["data"]["errorCode"] + "-" + requit["data"]["errorMsg"])
                raw_input("Press <enter>")

        else:
            print("授信接口调用异常！")
            raw_input("Press <enter>")
        return url, a, requit

    @wrapper
    def credit_inquiry(self):
        url = 'http://10.1.14.106:27405/channel/TEST/TCJQ/CREDIT_INQUIRY'
        data = {
                "channelCustId": "20200612886881021",
                "creditReqNo": "20200612668661021"
            }
        data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = self.creditReqNo
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

        }

        while True:
            a = "**********授信结果查询！**********"
            time.sleep(6)
            re = requests.post(url, data=json.dumps(data), headers=headers)
            requit = re.json()
            requit["data"] = eval(requit["data"])
            if re.status_code == 200:
                print("授信查询接口调用成功！")
                if requit["data"]["status"]=="01":
                    print(requit)
                    print("授信通过！")
                    break
                elif requit["data"]["status"]=="00":
                    print("授信中！")
                else:
                    print("授信失败！")
                    if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                        logging.ERROR(requit["data"]["errorCode"] + "-" + requit["data"]["errorMsg"])
                        raw_input("Press <enter>")
            else:
                print("授信查询接口调用异常！")
                raw_input("Press <enter>")
        return url, a, requit

    @wrapper
    def disburse_trial(self):
        url = 'http://10.1.14.106:27405/channel/TEST/TCJQ/DISBURSE_TRIAL'
        data = {
            "channelCustId": "20200612886881021",
            "periods": 6,
            "loanAmount": "1000.00"
        }
        data["channelCustId"] = self.channelCustId
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用试算！**********"
        print(a)
        res = requests.post(url,data=json.dumps(data),headers=headers)
        requit = res.json()
        requit["data"] = eval(requit["data"])
        time.sleep(3)
        if res.status_code == 200:
            print("支用试算接口调用成功！")
            if requit["data"]["status"]=="01":
                print(requit)
                capitalCode = requit["data"]["capitalCode"]
                print("支用试算成功！")
            else:
                print("支用试算失败！")
                raw_input("Press <enter>")
        else:
            print("支用试算接口调用异常！")
            raw_input("Press <enter>")
        return url, a, requit,capitalCode

    @wrapper
    def disburse(self,loanReqNo,capitalCode):
        url = 'http://10.1.14.106:27405/channel/TEST/TCJQ/DISBURSE'
        data = {
                "channelCustId": "20200612886881021",
                "loanReqNo": "202006128866881022",
                "creditReqNo": "20200612668661021",
                "loanAmount": "1000.00",
                "periods": 6,
                "purpose": "01",
                "bankCard": "6214852127765555",
                "bankCode": "308584000013",
                "bankName": "招商银行",
                "bankPhone": "13800000004",
                "longitude": "121.551738",
                "latitude": "31.224634",
                "ip": "192.168.1.2",
                "capitalCode":"HNTRUST",
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
        data["loanReqNo"] = loanReqNo
        data["creditReqNo"] = self.creditReqNo
        data["capitalCode"] = capitalCode
        print(data)
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用接口！**********"
        print(a)
        time.sleep(3)
        re = requests.post(url,data=json.dumps(data),headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            print("支用接口调用成功！")
            if requit["data"]["status"]=="01":
                print(requit)
                print("受理成功，处理中!")
            else:
                print("受理失败")
                if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                    logging.ERROR(requit["data"]["errorCode"]+"-"+requit["data"]["errorMsg"])
                    raw_input("Press <enter>")
        else:
            print("支用接口调用异常！")
            raw_input("Press <enter>")

        return url, a, requit

    @wrapper
    def disburse_in_query(self,loanReqNo):
        url = 'http://10.1.14.106:27405/channel/TEST/TCJQ/DISBURSE_IN_QUERY'
        data = {
                "channelCustId":"20200612886881021",
                "creditReqNo":"20200612668661021",
                "loanReqNo":"202006128866881022"
        }
        data["channelCustId"] = self.channelCustId
        data["loanReqNo"] = loanReqNo
        data["creditReqNo"] = self.creditReqNo
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用结果查询！**********"
        print(a)
        time.sleep(10)
        while True:
            re = requests.post(url, data=json.dumps(data), headers=headers)
            requit = re.json()
            requit["data"] = eval(requit["data"])
            if re.status_code == 200:
                print("支用结果查询接口调用成功！")
                if requit["data"]["status"]=="01":
                    print(requit)
                    print("支用成功")
                    break
                elif requit["data"]["status"]=="00":
                    print("处理中！")
                else:
                    print("支用失败！")
                    if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                        logging.ERROR(requit["data"]["errorCode"] + "-" + requit["data"]["errorMsg"])
                        raw_input("Press <enter>")
            else:
                print("支用结果查询接口调用异常！")
                raw_input("Press <enter>")
            time.sleep(10)
        return url, a, requit

def serial_number():
    a = str(random.randint(1, 1000))
    b = time.strftime("%Y%m%d%H%M%S")
    channelCustId = b + '68' + a
    creditReqNo = b + '86' + a
    loanReqNo = b + '686' + a
    return channelCustId,creditReqNo,loanReqNo

def phone():
    a = str(random.randint(1000,10000))
    b = time.strftime("%m%d")
    phone = "166"+b+a
    return phone


def name_idno():
    url = 'http://www.xiaogongju.org/index.php/index/id.html/id/513224/year/1990/month/10/day/30/sex/%E7%94%B7'

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
    ORANGE_name_idno = name_idno()
    ORANGE_phone = phone()
    ORANGE_serial_number = serial_number()
    hyzllg = Hyzllg(ORANGE_serial_number[0],ORANGE_serial_number[1], ORANGE_name_idno[0], ORANGE_name_idno[1],ORANGE_phone)
    test_info = f'''
            姓名：{ORANGE_name_idno[0]}
            身份证号：{ORANGE_name_idno[1]}
            手机号：{ORANGE_phone}
            channelCustId：{ORANGE_serial_number[0]}
            creditReqNo：{ORANGE_serial_number[1]}
            loanReqNo:{ORANGE_serial_number[2]}
            '''
    hyzllg.credit_granting()
    hyzllg.credit_inquiry()
    capitalCode_ = hyzllg.disburse_trial()
    hyzllg.disburse(ORANGE_serial_number[2],capitalCode_[-1])
    # hyzllg.disburse_in_query(ORANGE_serial_number[2])
    time.sleep(1)
    print(test_info)
    raw_input("Press <enter>")

if __name__ == '__main__':
    main()