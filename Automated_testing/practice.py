import requests
import json
import time
import sys

def wrapper(f):
    def inner():
        s = f()
        with open(r'C:\Users\16621\Desktop\hyzllg.log','a+',encoding='utf-8') as hyzllg:
            hyzllg.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s[0]} {s[1]} {s[2]}\n")
    return inner

@wrapper
def credit_inquiry():
    url = 'http://10.1.14.106:27405/channel/TEST/TCJQ/CREDIT_INQUIRY'
    data = {
        "channelCustId": "20200612886881021",
        "creditReqNo": "20200612668661021"
    }
    # data["channelCustId"] = self.channelCustId
    # data["creditReqNo"] = self.creditReqNo
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "10.1.14.106:27405",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

    }

    while True:
        a = "**********授信结果查询！**********"
        print(a)
        time.sleep(6)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200:
            print(requit)
        else:
            print("授信查询接口异常！")
            sys.exit()
        if 'status":"01' in requit["data"]:
            print("授信成功！进入下一环节！")
            break
        elif 'status":"02' in requit["data"]:
            print("授信失败！")
            sys.exit()
        else:
            enumerate
    return url,a,requit

credit_inquiry()