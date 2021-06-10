import json
import os
import random
import time
from hashlib import md5
import cx_Oracle

# 核心数据库配置
import requests

hxSIT_ORACLE = ["xbhxbusi", "ccic1234","10.1.12.141:1521/PTST12UF"]
hxDEV_ORACLE = ["xbhxbusi","ccic1234","10.1.12.141:1523/PDEV12UF"]
hxUAT_ORACLE = ["xbhxbusi","ccic1234","10.1.12.141:1521/puat12uf"]
# 账务数据库配置
zwSIT_ORACLE = ["gdbzdev", "ccic1234", "10.2.3.203:1521/R2TST16GPDB"]
zwUAT_ORACLE = ["gdbzbusi","ccic9879","10.2.3.203:1521/R2UAT16GPDB"]
#360
sit_url_360 = 'http://10.1.14.106:27405/channel/apitest/QFIN/'
uat_url_360 = 'http://10.1.14.117:27405/channel/apitest/QFIN/'
dev_url_360 = 'http://10.1.14.106:27405/channel-dev/apitest/QFIN/'
#还呗
sit_url_hb = 'http://10.1.14.106:27405/channel/apitest/HUANBEI/'
uat_url_hb = 'http://10.1.14.117:27405/channel/apitest/HUANBEI/'
dev_url_hb = 'http://10.1.14.106:27405/channel-dev/apitest/HUANBEI/'
#交行
sit_url_jh = 'http://10.1.14.106:27405/channel/apitest/BCM/'
uat_url_jh = 'http://10.1.14.117:27405/channel/apitest/BCM/'
dev_url_jh = 'http://10.1.14.106:27405/channel-dev/apitest/BCM/'
#甜橙
sit_url_tc = 'http://10.1.14.106:27405/channel/apitest/TCJQ/'
uat_url_tc = 'http://10.1.14.117:27405/channel/apitest/TCJQ/'
dev_url_tc = 'http://10.1.14.106:27405/channel-dev/apitest/TCJQ/'
#拍拍
sit_url_pp = 'http://10.1.14.106:27405/channel/TEST/PPDAI/'
uat_url_pp = 'http://10.1.14.117:27405/channel/apitest/PPDAI/'
dev_url_pp = 'http://10.1.14.106:27405/channel-dev/apitest/PPDAI/'



def loanReqNo():
    a = str(random.randint(1, 10000))
    b = time.strftime("%Y%m%d%H%M%S")
    loanReqNo = b + '88' + a
    return loanReqNo

def creditReqNo():
    a = str(random.randint(1, 10000))
    b = time.strftime("%Y%m%d%H%M%S")
    creditReqNo = b + '68' + a
    return creditReqNo

def channelCustId():
    a = str(random.randint(1, 10000))
    b = time.strftime("%Y%m%d%H%M%S")
    channelCustId = b + '86' + a
    return channelCustId

def phone():
    a = str(random.randint(1000, 10000))
    b = time.strftime("%m%d")
    phone = "166" + b + a
    return phone

def bankcard():
    a = str(random.randint(1000, 10000))
    b = time.strftime("%m%d%H%M%S")
    bankcard = '621466' + b
    return bankcard

def PMT(custGrde,periods,businessrate):#执行年利率，期数，客户等级
    import warnings
    #忽略警告
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    import numpy

    #PMT函数
    a = numpy.pmt(custGrde/100/12,periods,-1)
    b = numpy.pmt(businessrate/100/12,periods,-1)
    c = (a - b)*100
    pmt = round(c,3)
    return  abs(pmt)

def check_id_card(n):
    var = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    var_id = ['1', '0', 'x', '9', '8', '7', '6', '5', '4', '3', '2']
    n = str(n)
    sum = 0
    for i in range(0, 17):
        sum += int(n[i]) * var[i]
    sum %= 11
    if (var_id[sum]) == str(n[17]):
        return sum
    else:
        return 0

def sql_cha(cursor,my_sql_c):
    try:

        cursor.execute(my_sql_c)
        all_data = cursor.fetchall()
        oo = list(all_data)
        # conn.close()
        return oo
    except cx_Oracle.DatabaseError:
        return print("无效的SQL语句")

def sql_update(setting,v,vv):
    try:
        conns = cx_Oracle.connect(setting[0], setting[1], setting[2])
        cursor = conns.cursor()
        my_sql_c = "UPDATE system_setup SET businessdate = :v,batchdate = :vv".format()
        cursor.execute(my_sql_c, {'v': v,'vv': vv})
        conns.commit()  # 这里一定要commit才行，要不然数据是不会插入的
        conns.close()
        print("核心数据库时间更改成功  {}".format(v))

    except cx_Oracle.DatabaseError:
        return print("无效的SQL语句")
def test_api(url,data,title):

    print(title)
    print(f"请求报文：{data}")
    re = requests.post(url, data=json.dumps(data))
    requit = re.json()
    requit["data"] = eval(requit["data"])
    print(f"响应报文：{requit}")
    return requit

class id_card:
    def areaCodeDict(self,fileName):
        dataDict = {}
        key=0
        value=1
        dataLine=open(fileName,encoding="utf-8").read().splitlines()
        for line in dataLine:
            tmpLst=line.split(",")
            dataDict[tmpLst[key]]=tmpLst[value]
        return dataDict

    # 功能：随机生产一个区域码

    def areaCode(self,Dict):
        codeList=[]
        for key in Dict.keys():
            codeList.append(key)
        lenth=len(codeList)-1
        i=random.randint(0,lenth)
        return codeList[i]
    # 功能：随机生成1930年之后的出生日期
    def birthDay(self):
        # d1=datetime.datetime.strptime('1930-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        # d2=datetime.datetime.now()
        # delta=d2-d1
        # dys=delta.days
        # i=random.randint(0,dys)
        # dta=datetime.timedelta(days=i)
        # bhday=d1+dta
        # return bhday.strftime('%Y%m%d' )

        # 8位生日编码
        date_start = time.mktime((1990, 1, 1, 0, 0, 0, 0, 0, 0))
        date_end = time.mktime((1997, 8, 1, 0, 0, 0, 0, 0, 0))

        date_int = random.randint(date_start, date_end)
        id_date = time.strftime("%Y%m%d", time.localtime(date_int))
        return id_date

    #功能：随机生成3位序列号

    def ordrNum(self):
        odNum=random.randint(100,999) #随机生成100到999之间的3为数据
        sex=odNum%2
        return (str(odNum),sex)

    #功能：生成校验码

    def check(self,id_num):
        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
        checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
        for i in range(0,len(id_num)):
           count = count +int(id_num[i])*weight[i]
        return checkcode[str(count%11)] #算出校验码

    def generate_ID(self):
        while True:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            fileName = base_dir + r"\untitled\districtcode.txt"  # 区域文件地址
            areaCodeDt=self.areaCodeDict(fileName)   #调用生成字典
            areaCd=self.areaCode(areaCodeDt)     #生成区域码
            areaCdName=areaCodeDt[areaCd]   #获取区域名称
            birthDy=self.birthDay()   #生成出生日期
            (ordNum,sex)=self.ordrNum()  #生成顺序号和性别
            checkcode=self.check((areaCd+birthDy+ordNum)) #生产校验码
            id_card=areaCd+birthDy+ordNum+checkcode  #拼装身份证号

            if check_id_card(id_card):
                break
            else:
                continue

        return id_card

def random_name():
    # 删减部分，比较大众化姓氏
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"
    # 百家姓全部姓氏
    # firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平" \
    #             "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董粱杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮" \
    #             "龚程嵇邢滑裴陆荣翁荀羊於惠甄麴家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴欎胥能苍" \
    #             "双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍舄璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空" \
    #             "曾毋沙乜养鞠须丰巢关蒯相查後荆红游竺权逯盖益桓公晋楚闫法汝鄢涂钦归海帅缑亢况后有琴梁丘左丘商牟佘佴伯赏南宫墨哈谯笪年爱阳佟言福百家姓终"
    # 百家姓中双姓氏
    firstName2 = "万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空亓官司寇仉督子颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁段干百里东郭南门呼延羊舌微生梁丘左丘东门西门南宫南宫"
    # 女孩名字
    girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
    # 男孩名字
    boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
    # 名
    name = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'

    # 10%的机遇生成双数姓氏
    if random.choice(range(100)) > 10:
        firstName_name = firstName[random.choice(range(len(firstName)))]
    else:
        i = random.choice(range(len(firstName2)))
        firstName_name = firstName2[i:i + 2]

    sex = random.choice(range(2))
    name_1 = ""
    # 生成并返回一个名字
    if sex > 0:
        girl_name = girl[random.choice(range(len(girl)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        return firstName_name + name_1 + girl_name  # + "\t女"
    else:
        boy_name = boy[random.choice(range(len(boy)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        return firstName_name + name_1 + boy_name  # + "\t男"


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

#超级鹰打码平台
def dranformImgCode(imgPath, imgType):
    chaojiying = Chaojiying_Client('hyzllg', 'hyzllg', '918177')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(imgPath, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    return chaojiying.PostPic(im, imgType)["pic_str"]


