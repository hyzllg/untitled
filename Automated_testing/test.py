import requests





def update_lj_mock(api,loanNO,datetime):
    url = "http://10.1.14.146:7300/api/mock/update"
    headers = {
        "Content-Type":"application/json;charset=UTF-8",
        "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVmNjk0ZDQ0NmQ5ZGZjMmRkYTU1ODlhMSIsImlhdCI6MTYzMTI1Nzg5MSwiZXhwIjoxNjMyNDY3NDkxfQ.xahESAnAuiYd9yQftvvnJ0vGHc0AJYHqslrH05lBatY",
        "Cookie":"easy-mock_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVmNjk0ZDQ0NmQ5ZGZjMmRkYTU1ODlhMSIsImlhdCI6MTYzMTI1Nzg5MSwiZXhwIjoxNjMyNDY3NDkxfQ.xahESAnAuiYd9yQftvvnJ0vGHc0AJYHqslrH05lBatY",
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
	"url": "/std/loan/query",
	"mode": '{"data": {"code": 0,"message": "成功","data": {"loan_order_no": "%s","asset_status": "repay","grant_at": "%s"},"sucFlag": "true"}}' % (loanNO,datetime),
	"method": "post",
	"description": "借款申请结果查询",
	"id": "5fbe001bc9b25623b2c09d00"
}
    if api == "apply":
        requit = requests.post(url=url,headers=headers,json=loan_apply_datas)
        print(requit.json())
    elif api == "query":
        requit = requests.post(url=url, headers=headers, json=loan_apply_datas)
        print(requit.json())
    else:
        print("未知错误！")


update_lj_mock("apply","cjl20201123000000018","2021-09-10")