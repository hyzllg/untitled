import requests
from json import dumps
from utils import my_log

class request_api:
    def __init__(self):
        self.log = my_log.Log()
    def test_api(self , mode, url, data):
        try:
            self.log.info(f"请求报文：{data}")
            if mode.upper() == "POST":
                re = requests.request(mode, url, data=dumps(data))
                requit = re.json()
                requit["data"] = eval(requit["data"])
            elif mode.upper() == "GET":
                re = requests.request(mode, url, params=dumps(data))
                requit = re.json()
            self.log.info(f"响应报文：{requit}")
        except:
            requit = re.text
            print(re.text)
            print("接口响应异常")
        return requit