import requests
import json


url = 'http://10.1.14.191:26275/trial/loan'
data = {
	"reqNo":"d5f9634a87cb443889r2f7e1113f9c08",
	"systemCode":"SFPT",
	"version":"1",
	"businesstype":"7014",
	"orgid":"600000",
	"fundCode":"787",
	"repaymentmethod":"RPT000010",
	"businesssum":"8000.00",
	"putoutdate":"2020/04/10",
	"loanterm":6

}

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "10.1.14.191:26275",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}
a = "**********借款试算**********"
print(a)
print(f"请求报文：{data}")
# time.sleep(1)
re = requests.post(url, data=json.dumps(data), headers=headers)
requit = re.json()
print(f"响应报文：{requit}")
a = requit["data"]["nextpaydate"][-2:]
if a == "1" or a == "15":
    pass
