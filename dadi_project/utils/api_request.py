import requests
from json import dumps

class request_api:

    def test_api(self,url, data):
        try:
            print(f"请求报文：{data}")
            re = requests.post(url, data=dumps(data))
            requit = re.json()
            requit["data"] = eval(requit["data"])
            print(f"响应报文：{requit}")
        except:
            requit = re.text
            print(re.text)
            print("接口响应异常")
        return requit