import json

import requests

hyz = []
llg = {}

def insure_info():
    url = 'http://10.1.11.198:9001/llas-zuul/sfpt-external-platform-sp/sfpt/external/platform/sp/rule/bankcard'
    data = {
                "interfaceType":6,
                "productId":"7018",
                "mobile":"01234567890",
                "idCard":"012345678901234567",
                "applyNo":"demo22018101700000001",
                "source":"OLCICORE",
                "custName":"张三",
                "bankCard":"01234567890123456",
                "isAuth":1,
                "stage":"0",
                "accountNo":"01234567890123456"
                }

    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "10.1.14.106:27405",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }


    re = requests.post(url, data=json.dumps(data), headers=headers)
    requit = re.json()
    print(requit)

    a = requit["data"]["serviceCode"]
    hyz.append(a)

    print(requit)

for i in range(2):
    insure_info()
for i in hyz:
    if i not in llg:
        llg[i] = 1
    else:
        llg[i] += 1
for i in llg:
    print(f"{i} : {llg[i]}笔")