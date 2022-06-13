import requests
from utils import my_log

class request_api:
    def __init__(self):
        self.log = my_log.Log()
    def test_api(self , mode, url, data):
        global res, requit
        try:
            self.log.info(f"请求报文：{data}")
            if mode.upper() == "POST":
                res = requests.request(mode, url, json=data)
                requit = res.json()
                requit["data"] = eval(requit["data"])
            elif mode.upper() == "GET":
                res = requests.request(mode, url, json=data)
                requit = res.json()
            else:
                raise ValueError("异常")
            self.log.info(f"响应报文：{requit}")
        except:
            print(res.text)
            print("接口响应异常")
        return requit