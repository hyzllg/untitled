import os
import urllib
import requests
import Collect
import time
import re
from pprint import pprint
from lxml import etree
from bs4 import BeautifulSoup
from aip import AipSpeech
from flask import Flask,render_template
from selenium import webdriver


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

page_texts_dict = {}
urls_dict = {}

def git_img_url():
    #读取html文件
    fp = open('templates/html.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')

    page_texts = soup.select('.side-nav li')
    for i in page_texts:
        page_texts_dict[i['id'][0:4] + i['id'][-1]] = i.text.strip()
    for i in page_texts_dict.keys():
        a = soup.select(f'#{i} .page_text a')
        dirname = 'Imglibs'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        if not os.path.exists(dirname + '/' + page_texts_dict[i]):
            os.mkdir(dirname + '/' + page_texts_dict[i])
        for b in a:
            url_dict = {}
            url_dict[b.text.strip()] = b['href']
            urls_dict[page_texts_dict[i]] = url_dict
            page_text =b['href'] + b.text.strip()
            with open (dirname + '/' + page_texts_dict[i] + '/'+ 'url.txt','a',encoding='utf-8') as fp:
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
    -/crawler():直系文本内容
    -//crawler():全部文本内容
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
# url = 'https://www.kuaidaili.com/free/intr/%d/'
# ips = []
# for page in range(1,100):
#     new_url = format(url%page)
#     #让当次的请求使用代理机制，就可以更换请求的ip地址
# 	# page_text = requests.get(url=new_url,headers=headers,proxies={'http':ip:port}).text
#     page_text = requests.get(url=new_url,headers=headers).text
#
#     tree = etree.HTML(page_text)
#     #在xpath表达式中不可以出现tbody标签
#     tr_list = tree.xpath('//*[@id="list"]/table//tr')
#     for tr in tr_list:
#         ip = tr.xpath('./td[1]/text()')[0]
#         port = tr.xpath('./td[2]/text()')[0]
#         print(ip,port)
#         ips.append(ip)
#
# print(len(ips))

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
    
-使用流程：
    -点击控制台进行登录
    -选择想要实现的功能
    -实现功能下创建一个app
    -选择对应的pythonSDK文档进行代码实现

'''



def gushici_login():

    # 创建Session过cookie验证
    url_session = 'https://so.gushiwen.cn'
    session = requests.Session()
    session.get(url=url_session, headers=headers)

    #登录页面地址
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    #登录接口地址
    login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

    # 爬取验证码图片到本地 得到保存图片的本地地址
    page_text1 = session.get(url, headers=headers).text
    tree = etree.HTML(page_text1)
    src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    page_text2 = session.get(url=src, headers=headers).content
    with open('./yanzhengma.jpg', 'wb') as fp:
        fp.write(page_text2)
    #定义图片保存地址 并利用超级鹰打码解析验证码
    img_path = './yanzhengma.jpg'
    img_type = 1902
    code = Collect.dranformImgCode(img_path, img_type)
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
        "pwd": "Python_crawler",
        "code": code,
        "denglu": "登录"
    }
    page = session.post(url=login_url, headers=headers, data=data)
    page_text3 = page.text

    # 登录成功 实例储存
    with open('templates/html.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text3)


#需求
    #将段子王中的段子内容爬取到本地，然后基于语音合成将段子合成为mp3的音频文件，然后自己搭建一个web服务器，实时播放音频文件
    #爬取梨视频中的短视频数据，将最热板块下的短视频数据爬取且保存到本地
def get_duanziwang():#爬取段子网经典搞笑段子
    texts = {}
    duanziwang_url = 'https://www.duanziwang.com/t/57uP5YW456yR6K%2Bd.html'
    #网站证书过期，运行程序报错equests.exceptions.SSLError: HTTPSConnectionPool
    #requests.get()添加verify=False,
    # requests.packages.urllib3.disable_warnings()，添加一行代码，添加后可忽略告警
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url=duanziwang_url,headers=headers,verify=False)
    page_text = response.text
    # print(page_text)
    # xpath定位
    tree = etree.HTML(page_text)
    dl = tree.xpath('//div[@class="nr"]/dl')
    for i in dl:
        title = i.xpath('./span/dd/a/strong/text()')[0]
        dd = i.xpath('./dd/text()')
        text = ""
        for i in dd:
            i = i.strip("")
            text = text  + i
        texts[title] = text
        print(title)
        print(text,"\n")
    return texts


# get_duanziwang()

#Access Token获取
def get_Token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    Api_Key = 'QrIW0GXrg46p7qUbsrQq44wF'
    Secret_Key = 'wS2IROfaZy7d96EjjkT2dNu49Xce1qyh'
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={Api_Key}&client_secret={Secret_Key}'
    response = requests.get(host)
    page_dict = response.json()
    access_token = page_dict['session_key']
    t = page_dict['expires_in']/60/60
    print(f"token:{access_token}\n有效期：{t}小时")
    return access_token
# get_Token()

def esydl():
    """ 你的 APPID AK SK """
    #创建一个文件夹Mp3用来存放获取的MP3文件
    file_path = 'Mp3'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    APP_ID = '24350825'
    API_KEY = 'QrIW0GXrg46p7qUbsrQq44wF'
    SECRET_KEY = 'wS2IROfaZy7d96EjjkT2dNu49Xce1qyh'
    #新建AipSpeech
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    #获取到段子网段子
    texts = get_duanziwang()
    for i in texts.keys():
        #将获取到的段子利用百度AI语音合成技术，生成MP3语音文件
        result  = client.synthesis(texts[i], 'zh', 1, {
            'vol': 5,
        })
        if not isinstance(result, dict):
            with open(f'./{file_path}/{i}.mp3', 'wb') as f:
                f.write(result)
            print(i,"mp3语音文件获取成功！")
# esydl()



#爬取梨视频美式短视频
'''
梨视频爬取思路：
    将每一个视频详情页的url进行解析
    对视频详情页的url惊醒请求发送
    在视频详情页的页面源码中进行全局搜索，发现没有找到video标签
        视频标签是动态加载出来
        动态加载的数据方式
            ajax
            js
        在页面源码中搜索.mp4，定位到视频地址（存在于一组js代码）
            通过正则取出并发起请求
            
'''
def Li_videos():
    #header这个必须要加Referer，他妈的不加会报文章已下线
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'Referer': ''
    }
    #创建一个文件夹用来存放mp4小视频
    dirname = 'Mp4'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    Li_url = 'https://www.pearvideo.com/category_8'
    response = requests.get(url=Li_url,headers=headers)
    page_text = response.text
    tree = etree.HTML(page_text)
    #获取到短视频网页链接
    urls = tree.xpath('//div[@class="vervideo-bd"]/a')
    for i in urls:
        title = i.xpath('./div[2]/text()')[0]
        #利用re.sub去除非法字符，不然创建文件时会报错
        title = re.sub('[\/:*?"<>|]','',title)
        print(title)
        Referer = 'https://www.pearvideo.com' + '/' + i.xpath('./@href')[0]
        contId = Referer.split("_")[-1]
        header['Referer'] = Referer
        #視頻地址不在頁面源碼中，是通過js或ajax动态加载，访问ajax接口获取到视频地址
        videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}"
        # print(videoStatusUrl)
        #访问ajax接口获取视频地址
        resp = requests.get(url=videoStatusUrl,headers=header)
        #取出systemTime
        systemTime = resp.json()['systemTime']
        #取出srcUrl
        srcUrl = resp.json()['videoInfo']['videos']['srcUrl']
        #接口返回的地址,需要替换成真实的地址
        #https://video.pearvideo.com/mp4/adshort/20210611/1623396279075-15693739_adpkg-ad_hd.mp4  #404的地址
        #https://video.pearvideo.com/mp4/third/20210610/cont-1731794-11643402-111901-hd.mp4       #视频的真实地址
        #把接口返回的地址中的systemTime替换成视频id
        truthUrl = srcUrl.replace(systemTime,f'cont-{contId}')
        print(truthUrl)

        #发送请求下载视频文件
        Mp4_video = requests.get(url=truthUrl,headers=headers).content
        #保存mp4视频文件
        Mp4_path = dirname + '/' + title + re.findall(r'hd(.*)',truthUrl)[0]
        with open(Mp4_path,'wb') as fp:
            fp.write(Mp4_video)
        print(Mp4_path,"爬取成功！")

# Li_videos()


#12306余票检测
def get_12306(train_date,start_city,end_city):
    data = []
    url = 'https://kyfw.12306.cn/otn/leftTicket/query'
    prames = {
        "leftTicketDTO.train_date": train_date,
        "leftTicketDTO.from_station": start_city,
        "leftTicketDTO.to_station": end_city,
        "purpose_codes": "ADULT"
    }
    #请求接口需要传输cookie，利用session解决cookie反爬机制
    session = requests.Session()
    session.get(url='https://kyfw.12306.cn/',headers=headers)
    response = session.get(url=url,headers=headers,params=prames)
    page_texts = response.json()['data']['result']
    for page_text in page_texts:
        page_text = page_text.split('|')
        #状态
        status = page_text[1]
        #车票号
        train_no = page_text[2]
        # 车次
        station_train_code = page_text[3]
        # 起始站代号
        start_station_code = page_text[4]
        # 终点站代号
        end_station_code = page_text[5]
        # 出发站代号
        from_station_code = page_text[6]
        # 到达站代号
        to_station_code = page_text[7]
        # 出发时间
        start_time = page_text[8]
        # 到达时间
        arrive_time = page_text[9]
        # 运行时长
        run_time = page_text[10]
        # 是否可买
        can_buy = page_text[11]
        # 出发日期
        start_train_date = page_text[13]
        # 软卧
        rw_num = page_text[23]
        # 软座
        rz_num = page_text[24]
        tz_num = page_text[25]
        # 无座
        wz_num = page_text[26]
        yb_num = page_text[27]
        # 硬卧
        yw_num = page_text[28]
        # 硬座
        yz_num = page_text[29]
        # 二等座
        edz_num = page_text[30]
        # 一等座
        ydz_num = page_text[31]
        # 商务特等座
        swz_num = page_text[32]
        # 动卧
        dw_num = page_text[33]
        itme_dict = {
            '状态': status,
            '车次': station_train_code,
            '起始站代号': start_station_code,
            '终点站代号': end_station_code,
            '出发站代号': from_station_code,
            '到达站代号': to_station_code,
            '出发时间': start_time,
            '到达时间': arrive_time,
            '运行时长': run_time,
            '是否可买': can_buy,
            '出发日期': start_train_date,
            '软卧': rw_num,
            '软座': rz_num,
            '无座': wz_num,
            '硬卧': yw_num,
            '二等座': edz_num,
            '一等座': ydz_num,
            '商务特等座': swz_num,
            '动卧': dw_num
        }
        data.append(itme_dict)
    print(data)
    # for a in data[0].keys():
    #     print(a + '|', end="")
    # for i in data:
    #     print('\n')
    #     for b in i.values():
    #         print(b + '|' , end="")

train_date = "2021-06-20"
start_city = "ERN"
end_city = "SHH"


page_text = get_12306(train_date,start_city,end_city)






