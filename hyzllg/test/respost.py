import os
import urllib
from pprint import pprint

import requests
import re

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



# url = 'https://movie.douban.com/j/chart/top_list'
#
# params = {
#     "type": "5",
#     "interval_id": "100:90",
#     "action": "",
#     "start": "0",
#     "limit": "333"
#
# }
#
# response = requests.get(url,params=params,headers=headers)
# # response.encoding = 'utf-8'
# # page_text = response.json()
# page_text = response.json()
# print(page_text)
# for i in page_text:
#     title = i["title"]
#     score = i["score"]
#     types = i["types"]
#     regions = i["regions"]
#     url = i["url"]
#     release_date = i["release_date"]
#     actors = i["actors"]
#     datas = f"电影名：{title}\n评分：{score}\n电影类型：{types}\n国家：{regions}\n地址：{url}\n上映时间：{release_date}\n演员：{actors}\n"
#     print(datas)
#     with open ('./datas.txt' , 'a' , encoding='utf-8') as fp:
#         fp.write(datas)




img_ual = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201606%2F11%2F20160611170143_zGfvw.jpeg&refer=http%3A%2F%2Fb-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1625319680&t=91a63d1f7f54c20162e37af80ea0d476'

# #方式一
# response = requests.get(url=img_ual,headers=headers)
# img_data = response.content
# with open('./1.jpg','wb') as fp:
#     fp.write(img_data)

#方式二
# urllib.request.urlretrieve(img_ual,'./2.jpg')

#分析浏览器开发者工具中Elements和network这两个选项卡对应的页面源码数据有何不同之处
#elenments中包含的显示的页面源码数据为当前页面所有的的数据加载完毕后对应的万丈的页面源码数据（包含了加载的动态加载数据）
#network显示的页面源码数据仅仅为某一个单独的请求对应的响应数据（不包含动态加载的数据）
#如果在进行数据解析的时候，一定是需要对页面布局进行分析如果当前网站没有动态加载的数据就可以直接使用Elements对页面布局进行分析，否则只可以使用network对页面数据进行分析


#需求：爬取校花网中图片
url = 'www.521609.com'
#创建名字为imglibs的文件夹
dirname = 'Imglibs'
if not os.path.exists(dirname):
    os.mkdir(dirname)
#捕获到当前页面的页面源码数据
url_xiaohua = 'http://www.521609.com/tuku/'
response = requests.get(url=url_xiaohua,headers=headers)
response.encoding = "utf-8"
page_data = response.text
with open ('./11.txt' , 'w' , encoding='utf-8') as fp:
    fp.write(page_data)
# print(page_data)

######re.S重点 用来除去换行回车
ex = '<li>.*?<img src="(.*?)" alt='
img_src_list = re.findall(ex,page_data,re.S)
for src in img_src_list:
    src = 'http://www.521609.com' + src
    imgpath = dirname +'/' + src.split('/')[-1]
    #将照片下载到本目录imglibs文件夹内
    urllib.request.urlretrieve(src,imgpath)
    print(imgpath,"下载成功！")



