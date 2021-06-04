import os
import urllib
from pprint import pprint

import requests
import re

headers = {
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

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
url_xiaohua = f'https://goss.vcg.com/html/creativeSub/solartopic.html'
response = requests.get(url=url_xiaohua,headers=headers)
response.encoding = "utf-8"
page_data = response.text
with open ('./11.txt' , 'w' , encoding='utf-8') as fp:
    fp.write(page_data)
# print(page_data)

####re.S重点 用来除去换行回车
ex = '<div class=".*?<img src="(.*?)" alt="'
img_src_list = re.findall(ex,page_data,re.I|re.S|re.M)
print(img_src_list)
for src in img_src_list:
    src = 'https://goss.vcg.com/html/creativeSub/' + src
    imgpath = dirname +'/' + src.split('/')[-1]
    #将照片下载到本目录imglibs文件夹内
    urllib.request.urlretrieve(src,imgpath)
    print(imgpath,"下载成功！")



