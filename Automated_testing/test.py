import json

import requests


# def credit_inquiry():
#     url = 'http://10.1.14.106:27405/channel/apitest/TCJQ/CREDIT_INQUIRY'
#
#     data = {
#         "channelCustId": "20210526093908861869",
#         "creditReqNo": "20210526093908684052",
#         "creditApplyNo": "202105260000000002"
#     }
#
#     # headers = {
#     #     "Content-Type": "application/json;charset=UTF-8",
#     #     "Host": "10.1.14.106:27405",
#     #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
#     #
#     # }
#     # , headers = headers
#
#     a = "**********授信结果查询！**********"
#     print(a)
#     print(f"请求报文：{data}")
#     re = requests.post(url, data=json.dumps(data))
#     requit = re.json()
#     requit["data"] = eval(requit["data"])
#     print(f"响应报文：{requit}")


url = 'http://10.1.14.106:27405/channel/apitest/TCJQ/CREDIT_INQUIRY'
data = {
    "channelCustId": "20210526093908861869",
    "creditReqNo": "20210526093908684052",
    "creditApplyNo": "202105260000000002"
}
title = "**********授信结果查询！**********"
def test_api(url,data,title):

    print(title)
    print(f"请求报文：{data}")
    re = requests.post(url, data=json.dumps(data))
    requit = re.json()
    requit["data"] = eval(requit["data"])
    print(f"响应报文：{requit}")
    return requit

for i in range(1):
    test_api(url,data,title)