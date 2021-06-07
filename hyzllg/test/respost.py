import os
import urllib
from pprint import pprint
from lxml import etree
import time

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

'''
数据解析的作用？
    用来实现聚焦爬虫
网页中显示的数据都是存储在哪里？
    都是存储在html的标签中或者是标签的属性中
数据解析的通用原理是什么？
    指定标签的定位
    取出标签中存储的数据或则标签属性中的数据

##bs4
bs4解析原理
    实例化一个BeautifulSoup的对象，且将待解析的页面源码数据加载到该对象中
    调用BeautifulSoup对象中相关方法或则属性进行标签定位和文本数据的提取
环境安装
    pip install lxml #解析器
    pip install bs4
Beautifulsoup对象的实例化：
    Beautifulsoup(fp,'lxml'):用来将本地储存的html文档中的数据进行解析
    Beautifulsoup（page_text,'lxml'):用来将互联网中请求到的页面源码数据进行解析
标签定位
    soup.tagName:只可以定位到第一次出现的tagname标签
    soup.find('tagname',attrname='value'):属性定位
    soup.findall:跟find一样用作属性定位，只不过findall返回的是列表
    soup.select('选择器'):选择器定位
        类选择器
        id选择器
        层级选择器
            > : 表示一个层级
            空格 : 表示多个层级
取数据
    .text : 返回的是该标签下所有的文本内容
    .string : 返回的是该标签直系的文本内容
取属性
    tag['attrname']
'''


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

def get_books():
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    page_test = response.text
    #实例储存html
    # with open('./html.html','w',encoding='utf-8') as fp:
    #     fp.write(page_test)
    #数据解析
    # with open('./html.html','r',encoding='utf-8') as fp:
    #     datas = fp.read()
    soup = BeautifulSoup(page_test,'lxml')
    book_titles = soup.select('.book-mulu > ul > li > a')
    #写入文本
    fp = open('./sanguo.txt', 'a', encoding='utf-8')
    for i in book_titles:
        #获取章节名及对应章节内容
        book_url = 'https://www.shicimingju.com' + i['href']
        book_title = i.text
        response = requests.get(url=book_url,headers=headers)
        response.encoding='utf-8'
        page_test = response.text
        soup = BeautifulSoup(page_test,'lxml')
        div_tag = soup.find('div',class_='chapter_content')
        content = div_tag.text
        # content = soup.select('.chapter_content')[0].text
        fp.write(book_title + ':' + content + '\n')
        print(book_title,"爬取成功！")
    fp.close()



# get_books()

'''
xpath解析
环境安装
    -pip install lxml
解析原理：html标签是以树状的形式进行展示
    -实例化一个etree的对象，且将带解析的页面源码数据加载到该对象中
    -调用etree对象的xpath方法结合着不同的xpath表达式实现标签的定位和数据提取
实例化etree对象
    -etree.parse('filename'):将本地html文档加载到该对象中
    -etree.HTML(page_text):网站获取的页面数据加载到该对象
标签定位：
    -最左侧的/（忽略此种方法）：如果xpath表达式最左侧是以/开头则表示该xpath表达式一定要从根标签开始定位指定标签
    -非最左侧/：表示一个层级
    -非最左侧//：表示多个层级
    -最左侧的//：xpath表达式可以从任意位置进行标签定位
    -属性定位：tagname[@attrname='value']
    -索引定位：tag[index]:索引是从1开始
    -模糊匹配：
        -//div[contains(@class,'ng)]
        -//div[starts-with(@class,'tg')]
取文本
    -/test():直系文本内容
    -//test():全部文本内容
取属性
    -/@attrname
    
xpath表达式如何更加具有通用性？
    在xpath表达式中使用管道符分隔符的作用，可以表示管道符左右两侧的
    子xpath表达式同时生效或则一个生效



'''




#爬取多页
#定义一个通用模板

def get_img():
    dirname = 'Girlslib'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    url = 'http://pic.netbian.com/4kmeinv/index_%d.html'
    for i in range(1,2):
        if i == 1:
            new_url = 'http://pic.netbian.com/4kmeinv/'
        else:
            new_url = format(url%i)
        response = requests.get(new_url,headers=headers)
        response.encoding = 'gbk'
        page_text = response.text
        tree = etree.HTML(page_text)
        a = tree.xpath('//div[@class="slist"]/ul/li')
        # print(a)
        for i in a:
            title = i.xpath('./a/img/@alt')[0] + '.jpg'
            img_src = 'https://pic.netbian.com' + i.xpath('./a/img/@src')[0]
            img_path = dirname + "/" + title
            urllib.request.urlretrieve(img_src, img_path)
            print(title,"爬取成功！")
# start_time = time.time()
# get_img()
# end_time = time.time()
# print(f"消耗时间{(end_time-start_time)/60}分钟")



#爬取站长之家 简历模板
'https://sc.chinaz.com/'


def get_Resume():
    #创建文件夹
    dirname = 'Resume'#简历
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    url = 'https://sc.chinaz.com/jianli/'
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    # print(tree)
    a = tree.xpath('//div[@id="main"]/div/div')
    for i in a:
        jianli_url = 'http:' + i.xpath('./a/@href')[0]
        jianli_title = i.xpath('./a/img/@alt')[0]
        # print(jianli_url,jianli_title)
        response1 = requests.get(url=jianli_url,headers=headers)
        response1.encoding = 'utf-8'
        page_text1 = response1.text
        tree1 = etree.HTML(page_text1)
        try:
            jianli_get_url = tree1.xpath('//div[@class="down_wrap"]/div[2]/ul/li/a/@href')[0]
            # print(jianli_title.strip(),jianli_get_url)
            #下载简历模板文件
            dir_path = dirname + '/' + jianli_title.strip()
            res = requests.get(url=jianli_get_url,headers=headers).content
            with open(dir_path,'wb') as fp:
                fp.write(res)
            print(jianli_title.strip(),"爬取成功！")
        except BaseException:
            pass

# get_Resume()

#爬取站长之家 高清图片

def gaoing_img():
    url = 'https://sc.chinaz.com/tupian/index_%d.html'
    dirname = 'Gximgs'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    for i in range(1,3):
        if i == 1:
            new_url = 'https://sc.chinaz.com/tupian/'
        else:
            new_url = format(url%i)
        response = requests.get(url=new_url,headers=headers)
        response.encoding='utf-8'
        page_text = response.text
        # print(page_text)
        tree = etree.HTML(page_text)
        a = tree.xpath('//div[@class="pic_wrap"]/div/div/div/a')
        for i in a:
            title = i.xpath('./@alt')[0]
            img_url = 'https:' + i.xpath('./@href')[0]
            print(title,img_url)
            response1 = requests.get(url=img_url,headers=headers)
            response1.encoding='utf-8'
            page_text1 = response1.text
            # print(page_text1)
            tree1 = etree.HTML(page_text1)
            bs = tree1.xpath('//div[@class="dian"]/a')[0]
            img_path = dirname + '/' + title.strip()
            img_urls = bs.xpath('./@href')[0]
            lll = requests.get(url=img_urls,headers=headers).content
            with open(img_path,'wb') as fp:
                fp.write(lll)
            print(title,"爬取成功！")












gaoing_img()