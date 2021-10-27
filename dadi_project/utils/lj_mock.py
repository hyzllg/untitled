import requests

def esay_mock_login():
    url = "http://10.1.14.146:7300/api/u/login"
    data = {"name":"gdzwzj","password":"Pass01!"}
    response = requests.post(url,data)
    try:
        token = response.json()["data"]["token"]
    except:
        print("获取token失败！")
    return token
def update_lj_mock(api,loanNO,datetime):
    token = esay_mock_login()
    url = "http://10.1.14.146:7300/api/mock/update"
    headers = {
        "Content-Type":"application/json;charset=UTF-8",
        "Authorization":"Bearer " + token,
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Host":"10.1.14.146:7300"

    }
    loan_apply_datas = {
   "url": "/std/loan/apply",
   "mode": '{"data": {"code": 0,"message": "成功","data": {"loan_order_no": "%s"},"sucFlag": "true"}}' % (loanNO),
   "method": "post",
   "description": "借款申请",
   "id": "5fbf094bc9b25623b2c09d08"
}
    loan_query_datas = {
    "url":"/std/loan/query",
    "mode":'{"data": {"code": 0,"message": "成功","data": {"loan_order_no":"%s","create_at": "%s 10:00:00","grant_amount": "22000.00","period": "12","asset_status": "repay","grant_at": "%s","debt_no": "W%s"}}}' % (loanNO,datetime,datetime,loanNO),
    "method":"post",
    "description":"借款申请结果查询",
    "id":"5fbe001bc9b25623b2c09d00"
}
    if api == "apply":
        requit = requests.post(url=url,headers=headers,json=loan_apply_datas)
        response = requit.json()
        try:
            if response["success"] == True and response["message"] == "success":
                print(f"更改龙江mock借款申请接口参数成功！")
        except:
            print("更改龙江mock借款申请接口参数失败!")
    elif api == "query":
        requit = requests.post(url=url, headers=headers, json=loan_query_datas)
        response = requit.json()
        try:
            if response["success"] == True and response["message"] == "success":
                print(f"更改龙江mock借款申请接口结果查询参数成功!")
        except:
            print("更改龙江mock借款申请接口结果查询参数失败!")
    else:
        print("未知错误！")


#启用龙江放款mock
def start_lj_mock():
    import requests
    url = "http://10.1.14.191:26275/sys/setMockStatus?fundCode=20062&status=1"
    response = requests.request("GET", url)
    print("龙江放款mock开启成功！")