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

#
# #需求：爬取校花网中图片
# url = 'www.521609.com'
# #创建名字为imglibs的文件夹
# dirname = 'Imglibs'
# if not os.path.exists(dirname):
#     os.mkdir(dirname)
# #捕获到当前页面的页面源码数据
# url_xiaohua = f'https://goss.vcg.com/html/creativeSub/solartopic.html'
# response = requests.get(url=url_xiaohua,headers=headers)
# response.encoding = "utf-8"
# page_data = response.text
# with open ('html.html', 'w' , encoding='utf-8') as fp:
#     fp.write(page_data)
# # print(page_data)
#
# ####re.S重点 用来除去换行回车
# ex = '<div class=".*?<img src="(.*?)" alt="'
# img_src_list = re.findall(ex,page_data,re.I|re.S|re.M)
# print(img_src_list)
# for src in img_src_list:
#     src = 'https://goss.vcg.com/html/creativeSub/' + src
#     imgpath = dirname +'/' + src.split('/')[-1]
#     #将照片下载到本目录imglibs文件夹内
#     urllib.request.urlretrieve(src,imgpath)
#     print(imgpath,"下载成功！")


#数据解析的作用？
    #用来实现聚焦爬虫
#网页中显示的数据都是存储在哪里？
    #都是存储在html的标签中或者是标签的属性中
#数据解析的通用原理是什么？
    #指定标签的定位
    #取出标签中存储的数据或则标签属性中的数据

###bs4
#bs4解析原理
    #实例化一个BeautifulSoup的对象，且将待解析的页面源码数据加载到该对象中
    #调用BeautifulSoup对象中相关方法或则属性进行标签定位和文本数据的提取
#环境安装
    #pip install lxml #解析器
    #pip install bs4
#Beautifulsoup对象的实例化：
    #Beautifulsoup(fp,'lxml'):用来将本地储存的html文档中的数据进行解析
    #Beautifulsoup（page_text,'lxml'):用来将互联网中请求到的页面源码数据进行解析
#标签定位
    #soup.tagName:只可以定位到第一次出现的tagname标签
    #soup.find('tagname',attrname='value'):属性定位
    #soup.findall:跟find一样用作属性定位，只不过findall返回的是列表
    #soup.select('选择器'):选择器定位
        #类选择器
        #id选择器
        #层级选择器
            # > : 表示一个层级
            # 空格 : 表示多个层级
#取数据
    # .text : 返回的是该标签下所有的文本内容
    # .string : 返回的是该标签直系的文本内容
#取属性
    #tag['attrname']

from bs4 import BeautifulSoup



items_dict = {}
urls_dict = {}

def git_img_url():
    #读取html文件
    fp = open('./html.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')

    items = soup.select('.side-nav li')
    for i in items:
        items_dict[i['id'][0:4] + i['id'][-1]] = i.text.strip()
    for i in items_dict.keys():
        a = soup.select(f'#{i} .item a')
        dirname = 'Imglibs'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        if not os.path.exists(dirname + '/' + items_dict[i]):
            os.mkdir(dirname + '/' + items_dict[i])
        for b in a:
            url_dict = {}
            url_dict[b.text.strip()] = b['href']
            urls_dict[items_dict[i]] = url_dict
            page_text =b['href'] + b.text.strip()
            with open (dirname + '/' + items_dict[i] + '/'+ 'url.txt','a',encoding='utf-8') as fp:
                fp.write(page_text + '\n')


# git_img_url()




