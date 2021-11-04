import requests
from json import dumps
from utils import Log

class request_api:
    def __init__(self):
        self.log = Log.Log()
    def test_api(self,url, data):
        try:
            self.log.info(f"请求报文：{data}")
            re = requests.post(url, data=dumps(data))
            requit = re.json()
            requit["data"] = eval(requit["data"])
            self.log.info(f"响应报文：{requit}")
        except:
            requit = re.text
            print(re.text)
            print("接口响应异常")
        return requit