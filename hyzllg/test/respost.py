from pprint import pprint

import requests

headers = {
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}



# for i in range(1,11):
#     data = {
#         "on": "true",
#         "page": str(i),
#         "pageSize": "15",
#         "productName": "",
#         "conditionType": "1",
#         "applyname": ""
#
#     }
#
#     # 药监总局 = 'http://scxk.nmpa.gov.cn:81/xk/'
#     url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
#
#     response = requests.post(url,data=data,headers=headers)
#     # response.encoding = "utf-8"
#     page_test = response.json()
#     # pprint(page_test)
#     for i in page_test["list"]:
#         BUSINESS_LICENSE_NUMBER = i["BUSINESS_LICENSE_NUMBER"]#社会信用代码
#         EPS_NAME = i["EPS_NAME"]#企业名称
#         PRODUCT_SN = i["PRODUCT_SN"]#许可证编号
#         QF_MANAGER_NAME = i["QF_MANAGER_NAME"]#发证机关
#         XC_DATE = i["XC_DATE"]#发证日期
#         XK_DATE = i["XK_DATE"]#有效期至
#         datas = (f'''
#         社会信用代码：{BUSINESS_LICENSE_NUMBER}
#         企业名称：{EPS_NAME}
#         许可证编号：{PRODUCT_SN}
#         发证机关：{QF_MANAGER_NAME}
#         发证日期：{XC_DATE}
#         有效期至：{XK_DATE}
#         ''')
#         print(datas)
#         with open ('./datas.txt' ,'a',encoding='utf-8') as fp:
#             fp.write(datas)



url = 'https://movie.douban.com/j/chart/top_list'

params = {
    "type": "5",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "100"

}

response = requests.get(url,params=params,headers=headers)
# response.encoding = 'utf-8'
# page_text = response.json()
page_text = response.json()
print(page_text)
for i in page_text:
    title = i["title"]
    score = i["score"]
    types = i["types"]
    regions = i["regions"]
    url = i["url"]
    release_date = i["release_date"]
    actors = i["actors"]
    datas = f"电影名：{title}\n评分：{score}\n电影类型：{types}\n国家：{regions}\n地址：{url}\n上映时间：{release_date}\n演员：{actors}\n"
    print(datas)
    with open ('./datas.txt' , 'a' , encoding='utf-8') as fp:
        fp.write(datas)
