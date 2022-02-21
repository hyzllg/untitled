import time
import requests
import random
import yaml
import os

def esay_mock_login():
    url = "http://10.1.14.146:7300/api/u/login"
    data = {"name":"gdzwzj","password":"Pass01!"}
    response = requests.post(url,data)
    try:
        token = response.json()["data"]["token"]
    except:
        print("获取token失败！")
    return token

#启用龙江放款mock
def start_lj_mock():
    import requests
    url = "http://10.1.14.191:26275/sys/setMockStatus?fundCode=20062&status=1"
    response = requests.request("GET", url)
    print("龙江放款mock开启成功！")

def random_number_reqno():
    a = str(random.randint(1, 100000))
    b = time.strftime("%Y%m%d%H%M%S")
    reqno = b + a
    return reqno
def update_lj_mock(api,loanNO,datetime,status):
    #获取配置信息
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    path = os.path.dirname(__file__)
    conf = get_yaml_data(f'{path}/conf/code_library.yaml')
    #获取龙江放款状态码值配置
    asset_status = conf['lj_putout_status']
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
    "mode":'{"data": {"code": 0,"message": "成功","data": {"loan_order_no":"%s","create_at": "%s 10:00:00","grant_amount": "22000.00","period": "12","asset_status": "%s","grant_at": "%s","debt_no": "W%s"}}}' % (loanNO,datetime,asset_status[status],datetime,loanNO),
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
start_lj_mock()
ljreqno = random_number_reqno()
loan_datetime=time.strftime("%Y-%m-%d")
'''
  0 : commit #审核中
  1 : pass #审核通过
  2 : grant #放款中
  3 : repay #放款成功
  4 : payoff #已结清
  5 : invalid #已失效
  6 : refused #审核不通过
  7 : failed #放款失败
'''
update_lj_mock("apply", ljreqno, loan_datetime,3)
update_lj_mock("query", ljreqno, loan_datetime,3)
# time.sleep(3)

