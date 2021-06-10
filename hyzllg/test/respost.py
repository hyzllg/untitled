import os
import urllib
from pprint import pprint
from lxml import etree
from bs4 import BeautifulSoup
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


站长素材高清图片下载
    反爬机制：图片懒加载，广泛应用在了一些图片的网站中
        只有当图片被显示在浏览器可视化范围内才会将img的伪属性变成真正的属性，如果是requests发起的请求，
        requests请求是没有可视化范围，因此我们一定要解析的是img伪数据的属性值（图片地址）
学过的反爬机制
    robots
    ua伪装
    动态加载数据的捕获
    图片懒加载

'''


#爬取多页
#定义一个通用模板

def get_img():
    dirname = 'Girlslib'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    url = 'http://pic.netbian.com/4kmeinv/index_%d.html'
    #for循环爬取多页
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

#爬取站长之家 高清图片 有反爬机制懒加载 需处理 解析img伪数据的属性值
def gaoing_img():
    url = 'https://sc.chinaz.com/tupian/index_%d.html'
    #创建一个目录
    dirname = 'Gximgs'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    #地址
    new_url = 'https://sc.chinaz.com/tupian/siwameinvtupian.html'

    response = requests.get(url=new_url,headers=headers)
    response.encoding='utf-8'
    #获取到html数据
    page_text = response.text
    #解析数据
    tree = etree.HTML(page_text)
    #定位
    a = tree.xpath('//div[@id="container"]/div/div/a')
    for i in a:
        #定位
        title = i.xpath('./img/@alt')[0]
        #获取到图片地址
        img_url = 'https:' + i.xpath('./img/@src2')[0]
        #设置图片保存路径
        img_path = dirname + "/" + title + ".jpg"
        #下载
        requit = requests.get(url=img_url,headers=headers).content
        with open(img_path,'wb') as fp:
            fp.write(requit)
        print(title,"爬取成功！")

# gaoing_img()


'''
*cookie
*代理机制
*验证码的识别
*模拟登录

-cookie
    是存储在客户端的一组键值对
    web中cookie的典型应用
        -免密登录
    cookie和爬虫之间的关联
        -sometimes，对一张页面进行请求的时候，如果请求的过程中不携带
         cookie的话，那么我们是无法请求到正确的页面数据，因此cookie是爬虫中一个非常典型且常见的反爬机制
         
-代理操作
    -在爬虫中，所谓的代理指的是什么？
        -就是代理服务器
    -代理服务器的作用是什么？
        -就是用来转发请求和响应
    -在爬虫中为什么需要使用代理服务器？
        -如果我们的爬虫在短时间内对服务器发起了高频的请求，那么服务器会检测到这样的一个异常的行为请求，就会将该请求对应设备的ip禁掉，就以为client设备
         无法对该服务器再次进行请求发送（ip被禁掉了）
        -如果ip被禁，我们就可以使用代理服务器进行请求转发，破解ip被禁的反扒机制，因为使用代理后，服务器链接受到的请求对应的ip地址就是代理服务器而不是我们真正的客户端的
    -代理服务器分为不同的匿名度：
        -透明代理：如果使用了该形式的代理，服务端就知道你使用了代理机制也知道你的真实ip
        -匿名代理：如果你使用代理，但是不知道你的真实ip
        -高匿代理：不知道你使用了代理也不知道你的真实ip
    -代理的类型
        -https：代理只能转发https协议的请求
        -http：转发http的请求
    -代理服务器：
        -快代理
        -西祠代理
        -goubanjia
        -代理精灵 http://zhiliandaili.cn/
            

'''
'''
-需求：爬取雪球网站中的咨询信息 https://xueqiu.com/
-分析
    -判定爬取的咨询数据是否为动态加载的
        -相关的更多咨询数据是动态加载的，滚轮滑动到底部的时候会动态加载出更多的咨询数据
    -定位到ajzx请求的数据包，提取出请求的url，响应数据为json形式的咨询数据
        {'error_description': '遇到错误，请刷新页面或者重新登录帐号后再试', 'error_uri': '/statuses/hot/listV2.json', 'error_data': None, 'error_code': '400016'}
        -问题：我们没有请求到想要的数据
        -原因：我们没有严格意义上模拟浏览器发请求
            -处理：可以将浏览器发请求携带的请求头，全部粘贴在headers字典中，将headers作用到requests的请求操作中即可
            -cookie的处理方式
                -方式一：手动处理
                    -将抓包工具中cookie粘贴在headers中
                    -弊端：cookie如果过了有效时常则该方式失效
                -方式二：自动处理
                    -基于session对象实现自动处理
                    -如何获取一个session对象：requests.Session()返回一个session对象
                    -session对象的作用：
                        -该对象可以向requests一样调用get和post发起指定的请求，只不过如果在使用session发请求的过程中如果产生了cookie，
                         则cookie会被自动储存到该session对象中，那么就意味着下次再次使用session对象发起请求，则该次请求就是携带cookie进行的请求发送
                        -在爬虫中使用session的时候，session对象至少会被使用几次？
                         -两次 第一次使用session是为了将cookie捕获且储存到session对象中，下次的时候就是携带cookie进行的请求发送
                         
            
'''
# #创建session对象
# #第一次使用session捕获且储存cookie，猜测雪球网的首页发起的请求可能会产生cookie
# main_url = 'https://xueqiu.com/'
# #获取一个session对象
# session = requests.Session()
# session.get(main_url,headers=headers)
# url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=213415&size=15'
# cookie = ''
# page_text = session.get(url,headers=headers).json()
# pprint(page_text)

'''

'''
# #封装一个代理池
# url = ''
# page_text = requests.get(url,headers=headers).text
# tree = etree.HTML(page_text)
# proxy_list = tree.xpath()
# http_proxy = []#代理池
# for proxy in proxy_list:
# 	dic = {
# 		'http':proxy
# 	}
# 	http_proxy.append(dic)
# http_proxy


#url模板
url = 'https://www.kuaidaili.com/free/intr/%d/'
ips = []
for page in range(1,100):
    new_url = format(url%page)
    #让当次的请求使用代理机制，就可以更换请求的ip地址
	# page_text = requests.get(url=new_url,headers=headers,proxies={'http':ip:port}).text
    page_text = requests.get(url=new_url,headers=headers).text

    tree = etree.HTML(page_text)
    #在xpath表达式中不可以出现tbody标签
    tr_list = tree.xpath('//*[@id="list"]/table//tr')
    for tr in tr_list:
        ip = tr.xpath('./td[1]/text()')[0]
        port = tr.xpath('./td[2]/text()')[0]
        print(ip,port)
        ips.append(ip)

print(len(ips))

'''
-验证码的识别
	-基于线上的打码平台识别验证码
	-打码平台
		-1、超级鹰
			-1、注册
            -2、登录
                -1、查询余额，充值
                -2、创建一个软件ID
                -3、下载示例代码
		-2、云打码
		-3、打码兔

'''
'''
-模拟登录
    -流程
        -对点击登录按钮对应的请求进行发送（post请求）
        -处理请求参数
            -用户名
            -密码
            -验证码
            -其他的防伪参数
-在请求参数中如果看到了一组乱序的请求参数，最好取验证码这组请求参数是否为动态化
    -处理
        方式一：常规来讲一般动态变化的请求参数会被隐藏在前台页面中，那么我们就要去前台页面源码中去找
        方式二：如果前台页面如果没有的话，我们就可以基于抓包工具进行全局搜索


-基于百度AI实现的爬虫功能
    -图像识别
    -语音识别&合成
    -自然语言处理

'''
# !/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


def dranformImgCode(imgPath, imgType):
    chaojiying = Chaojiying_Client('hyzllg', 'hyzllg', '918177')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(imgPath, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    return chaojiying.PostPic(im, imgType)["pic_str"]


# print(dranformImgCode('./a.jpg',1902))


# 创建Session过cookie验证
url_session = 'https://so.gushiwen.cn'
session = requests.Session()
session.get(url=url_session, headers=headers)

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

# 爬取验证码图片到本地 得到保存图片的本地地址
page_text1 = session.get(url, headers=headers).text
tree = etree.HTML(page_text1)
src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
page_text2 = session.get(url=src, headers=headers).content
with open('./yanzhengma.jpg', 'wb') as fp:
    fp.write(page_text2)

img_path = './yanzhengma.jpg'
img_type = 1902
code = dranformImgCode(img_path, img_type)
print(f"验证码：{code}")
__VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
print(f"__VIEWSTATE:{__VIEWSTATE}")
__VIEWSTATEGENERATOR = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
print(f"__VIEWSTATEGENERATOR:{__VIEWSTATEGENERATOR}")
data = {
    "__VIEWSTATE": __VIEWSTATE,
    "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
    "from": "http://so.gushiwen.cn/user/collect.aspx",
    "email": "16621381003@163.com",
    "pwd": "hyzllg",
    "code": code,
    "denglu": "登录"
}
page = session.post(url=login_url, headers=headers, data=data)
page_text3 = page.text

# 登录成功 实例储存
with open('./html.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text3)






