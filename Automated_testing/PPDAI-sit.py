import random
import requests
import logging
import json
import time
import re
import os
from past.builtins import raw_input



class Hyzllg:
    def __init__(self,loanReqNo,creditReqNo,name,idNo,phone,loanAmount,periods,bankCard,bankName,bankPhone):
        self.loanReqNo = loanReqNo
        self.creditReqNo = creditReqNo
        self.name = name
        self.idNo = idNo
        self.phone = phone
        self.loanAmount = loanAmount
        self.periods = periods
        self.bankCard = bankCard
        self.bankName = bankName
        self.bankPhone = bankPhone

    def wrapper(func):
        def inner(*args,**kwargs):
            s = func(*args,**kwargs)
            with open(os.path.join(os.path.expanduser("~"), 'Desktop')+"\PPDAI.log", 'a+', encoding='utf-8') as hyzllg:
                hyzllg.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s[0]} {s[1]} {s[2]}")
            return s

        return inner

    @wrapper
    def insure_info(self):
        url = 'http://10.1.14.106:27405/channel/TEST/PPDAI/INSURE_INFO'
        data = {
                "channelCustId":"",
                "insuranceNo":"2020082066566007",
                "name":"薛芒乙",
                "idNo":"513436199003021045",
                "idAddress":"浙江省杭州市江干区高教路119号",
                "phone":"16608205407",
                "amount":"5000",
                "periods":"12",
                "purpose":"01",
                "capitalCode":"FBBANK",
                "custGrde":"GRD36",
                "email":"ybhdsg@hrtx.com",
                "contactPhone":"17613145209",
                "callbackUrl":"callbackUrl"
            }

        data["insuranceNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        # print(data)
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********投保信息接口！**********"
        print(a)
        # time.sleep(1)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            print(requit)
            print("投保信息接口成功！")
            if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                print(f'errormsg:{requit["data"]["errorCode"] + requit["data"]["errorMsg"]}')
                raw_input("Press <enter>")
        else:
            print("投保信息接口异常！")
            raw_input("Press <enter>")
        return url,a,requit

    @wrapper
    def insure_data_query(self):
        url = 'http://10.1.14.106:27405/channel/TEST/PPDAI/INSURE_DATA_QUERY'
        data = {
            "loanReqNo": "20200613910199001"
        }
        data["loanReqNo"] = self.loanReqNo
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a =  "**********投保资料查询接口！**********"
        print(a)
        # time.sleep(1)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            print(requit)
            print("投保资料查询成功！")
        else:
            print("投保资料查询接口异常！")
            raw_input("Press <enter>")
        return url,a,requit,requit["data"]["premiumRate"]

    @wrapper
    def insure(self,a):
        url = 'http://10.1.14.106:27405/channel/TEST/PPDAI/INSURE'
        data = {
                "agentNo":"DingSheng",
                "agentName":"鼎盛保险经纪",
                "loanReqNo":"2020082066566007",
                "insReqNo":"2020082066566007",
                "name":"薛芒乙",
                "idNo":"513436199003021045",
                "phone":"16608205407",
                "amount":"5000",
                "periods":"12",
                "purpose":"01",
                "premiumRate":"1.417",
                "insurantName":"富邦华一银行有限公司",
                "insurantAdd":"上海浦东新区1239号",
                "postCode":"200300",
                "version":"DS_7018_V1.0",
                "docVersion":"V2.0-20200708"
            }
        data["loanReqNo"] = self.loanReqNo
        data["insReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        data["premiumRate"] = a
        # print(data)
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********投保接口！**********"
        print(a)
        # time.sleep(1)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            try:
                if requit["data"]["message"]:
                    print("受理失败")
                    print(f'errormsg:{requit["data"]["message"]}')
                    raw_input("Press <enter>")
            except BaseException as e:
                if requit["data"]["status"]=='01':
                    print(requit)
                    print("已受理，处理中！")
        else:
            print("投保接口调用异常！")
            raw_input("Press <enter>")
        return url,a,requit

    @wrapper
    def credit_granting(self):
        url = 'http://10.1.14.106:27405/channel/TEST/PPDAI/CREDIT_GRANTING'
        data = {
                "channelCustId":"",
                "insuranceNo":"2020082066566007",
                "creditReqNo":"2020082088588007",
                "name":"薛芒乙",
                "spelling":"",
                "sex":"00",
                "nationality":"中国",
                "nation":"汉族",
                "birthday":"1985/06/02",
                "idType":"00",
                "loanAmount":5000,
                "periods":12,
                "idNo":"513436199003021045",
                "phone":"16608205407",
                "idStartDate":"2016/01/18",
                "idEndDate":"2036/01/18",
                "idOffice":"浩然天下宝瓶洲大骊王朝落坡山办祖师堂",
                "idAddress":"浙江省杭州市江干区高教路119号",
                "marriage":"00",
                "children":"",
                "supplyPeople":0,
                "house":"",
                "addProvince":"",
                "addCity":"",
                "addDistrict":"",
                "addDetail":"",
                "industry":"C",
                "profession":"profession",
                "workplaceName":"大地保险公司",
                "workTel":"",
                "workProvince":"",
                "workCity":"",
                "workDistrict":"",
                "workDetailAdd":"",
                "workAge":0,
                "income":"01",
                "education":"05",
                "school":"",
                "email":"ybhdsg@hrtx.com",
                "contacts":[
                    {
                        "relation":"00",
                        "name":"哑巴湖大水怪",
                        "phoneNo":"17613145210"
                    },
                    {
                        "relation":"00",
                        "name":"哑巴湖大水怪",
                        "phoneNo":"17613145210"
                    }
                ],
                "bankCard":"6230523610012118577",
                "bankName":"中国农业银行",
                "bankPhone":"17613145209",
                "applyProvince":"",
                "applyCity":"",
                "applyDistrict":"",
                "purpose":"01",
                "direction":"",
                "payType":"",
                "payMerchantNo":"",
                "authFlag":"01",
                "deviceDetail":{
                    "deviceId":"",
                    "mac":"",
                    "longitude":"",
                    "latitude":"",
                    "gpsCity":"",
                    "ip":"",
                    "ipCity":"",
                    "oS":"ios"
                },
                "channelDetail":{
                    "capitalCode":"FBBANK",
                    "custGrde":"GRD36",
                    "applyEntry":"applyEntry",
                    "faceRecoType":"LINKFACE",
                    "faceRecoScore":99,
                    "creditDuration":"2020/08/19",
                    "currLimit":50000,
                    "currRemainLimit":50000,
                    "firstLoanFlag":"Y",
                    "overdueFlag":"N",
                    "settleLoanNum":0,
                    "unsettleLoanLimit":0,
                    "unsettleLoanNum":0,
                    "longestOverPeriod":0,
                    "compScore":"1",
                    "realFaceCheckResult":"1",
                    "citizenshipCheckResult":"1",
                    "bankCheckResult":"1",
                    "telcoCheckResult":"1"
                },
                "docDate":"2020/09/09"
            }
        data["insuranceNo"] = self.loanReqNo
        data["creditReqNo"] = self.creditReqNo
        data["name"] = self.name
        data["phone"] = self.phone
        data["idNo"] = self.idNo
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankCard
        data["bankName"] = self.bankName
        data["bankPhone"] = self.bankPhone
        # print(data)
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********授信接口！**********"
        print(a)
        # time.sleep(1)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200 :
            try:

                if requit["data"]["status"]=="01":
                    print(requit)
                    print("授信受理成功，处理中！")
                elif requit["data"]["status"]=="00":
                    print(requit)
                    print("受理失败！")
                    if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                        print(f'errormsg:{requit["data"]["errorCode"] + requit["data"]["errorMsg"]}')
                        raw_input("Press <enter>")
            except BaseException as e:
                if requit["data"]["message"]:
                    print(f'error:{requit["data"]["message"]}')


        else:
            print("授信接口调用异常！")
            raw_input("Press <enter>")
        return url,a,requit

    @wrapper
    def credit_inquiry(self):
        url = 'http://10.1.14.106:27405/channel/TEST/PPDAI/CREDIT_INQUIRY'
        data = {
                    "channelCustId":"",
                    "creditReqNo":"2020082088588007"
                }
        # data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = self.creditReqNo
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

        }
        number = 0
        while number <= 10 :
            a = "**********授信结果查询！**********"
            print(a)
            time.sleep(5)
            re = requests.post(url, data=json.dumps(data), headers=headers)
            requit = re.json()
            requit["data"] = eval(requit["data"])
            if re.status_code == 200:
                print("授信查询接口调用成功！")
                try:
                    if requit["data"]["status"]=="01":
                        print(requit)
                        print("授信通过！")
                        break
                    elif requit["data"]["status"]=="00":
                        print("授信中！")
                    else:
                        print("授信失败！")
                        if requit["data"]["message"]:
                            print(f'errormsg:{requit["data"]["message"]}')
                            raw_input("Press <enter>")
                except BaseException as e:
                    print(f'orrer:{requit["data"]["message"]}')
                    raw_input("Press <enter>")

            else:
                print("授信查询接口调用异常！")
                raw_input("Press <enter>")
            number += 1
        if number >= 10:
            raw_input("Press <enter>")

        return url, a, requit

    @wrapper
    def disburse(self):
        url = 'http://10.1.14.106:27405/channel/TEST/PPDAI/DISBURSE'
        data = {
                    "channelCustId":"",
                    "loanReqNo":"202008206656600622",
                    "insuranceNo":"",
                    "creditReqNo":"202008206656600622"
                }
        data["creditReqNo"] = self.creditReqNo
        data["loanReqNo"] = self.loanReqNo
        # print(data)
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用接口！**********"
        print(a)
        # time.sleep(1)
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200 :
            try:

                if requit["data"]["status"]=="01":
                    print(requit)
                    print("支用受理成功，处理中！")
                elif requit["data"]["status"]=="00":
                    print(requit)
                    print("支用受理失败！")
                    if requit["data"]["errorCode"] or requit["data"]["errorMsg"]:
                        print(f'errormsg:{requit["data"]["errorCode"] + requit["data"]["errorMsg"]}')
                        raw_input("Press <enter>")
            except BaseException as e:
                if requit["data"]["message"]:
                    print(f'error:{requit["data"]["message"]}')


        else:
            print("支用接口调用异常！")
            raw_input("Press <enter>")
        return url,a,requit


    @wrapper
    def disburse_in_query(self):
        url = 'http://10.1.14.106:27405/channel/TEST/PPDAI/DISBURSE_IN_QUERY'
        data = {
                "channelCustId":"",
                "creditReqNo":"132123123",
                "loanReqNo":"202002202002200220"
            }
        data["creditReqNo"] = self.creditReqNo
        data["loanReqNo"] = self.loanReqNo
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

        }

        while True:
            a = "**********支用结果查询！**********"
            print(a)
            time.sleep(6)
            re = requests.post(url, data=json.dumps(data), headers=headers)
            requit = re.json()
            requit["data"] = eval(requit["data"])
            if re.status_code == 200:
                print("支用查询接口调用成功！")
                try:
                    if requit["data"]["status"]=="01":
                        print(requit)
                        print("支用通过！")
                        break
                    elif requit["data"]["status"]=="00":
                        print("支用中！")
                    else:
                        print("支用失败！")
                        if requit["data"]["message"]:
                            print(f'errormsg:{requit["data"]["message"]}')
                            raw_input("Press <enter>")
                except BaseException as e:
                    print(f'orrer:{requit["data"]["message"]}')
                    raw_input("Press <enter>")

            else:
                print("支用询接口调用异常！")
                raw_input("Press <enter>")
        return url, a, requit
def loanReqNo():
    a = str(random.randint(1, 1000))
    b = time.strftime("%Y%m%d%H%M%S")
    loanReqNo = b + '88' + a
    return loanReqNo

def creditReqNo():
    a = str(random.randint(1, 10000))
    b = time.strftime("%Y%m%d%H%M%S")
    creditReqNo = b + '68' + a
    return creditReqNo

def phone():
    a = str(random.randint(1000,10000))
    b = time.strftime("%m%d")
    phone = "166"+b+a
    return phone


def name_idno():
    url = f'http://www.xiaogongju.org/index.php/index/id.html/id/513436/year/1990/month/{time.strftime("%m")}/day/{time.strftime("%d")}/sex/%E7%94%B7'

    headers = {
        "Content-Type":"text/html;charset=utf-8",
        "Host":"www.xiaogongju.org",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    print("*********爬取姓名身份证信息*********")
    request = requests.get(url,headers=headers)
    ret = request.text
    ret = re.findall('\s<td>\w*</td>',ret)
    new_ret = []
    for i in ret:
        i = i.replace(' ','')
        i = i.replace('<td>','')
        i = i.replace('</td>','')
        new_ret.append(i)
    print(new_ret)
    return new_ret


def get_districtcodes():
    districtcodes = []
    with open(os.path.join(os.path.expanduser("~"), 'Desktop')+"\districtcode.txt", mode='r', encoding='utf-8') as f:
        for l in f.readlines():
            districtcodes.append(l.strip()[:6])
    return districtcodes


def generate_ID(gender=None):
    """
    :param gender: 控制性别，None为随机, 1:男，0：女
    :return: 身份证号码
    """

    # 6位地址码
    codelist = get_districtcodes()
    id_location = codelist[random.randint(0, len(codelist)-1)]   # randint为闭区间，注意-1

    # 8位生日编码
    date_start = time.mktime((1990, 1, 1, 0, 0, 0, 0, 0, 0))
    date_end = time.mktime((1998, 8, 1, 0, 0, 0, 0, 0, 0))

    date_int = random.randint(date_start, date_end)
    id_date = time.strftime("%Y%m%d", time.localtime(date_int))

    # 3位顺序码，末尾奇数-男，偶数-女
    id_order = 0
    if not gender:
        id_order = random.randint(0, 999)
    elif gender == 1:
        id_order = random.randint(0, 499) * 2 + 1
    elif gender == 0:
        id_order = random.randint(0, 499) * 2

    if id_order >= 100:
        id_order = str(id_order)
    elif id_order >= 10:
        id_order = "0" + str(id_order)
    else:
        id_order = "00" + str(id_order)


    # 前17位相加
    ID_former = id_location + id_date + id_order

    # 验证码
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    cheack_code = {
        '0': '1',
        '1': '0',
        '2': 'X',
        '3': '9',
        '4': '8',
        '5': '7',
        '6': '6',
        '7': '5',
        '8': '5',
        '9': '3',
        '10': '2'}  # 校验码映射

    sum = 0
    for i, num in enumerate(ID_former):
        sum += int(num) * weight[i]
    ID_check = cheack_code[str(sum % 11)]

    ID = ID_former + ID_check
    return ID



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
        return firstName_name + name_1 + girl_name #+ "\t女"
    else:
        boy_name = boy[random.choice(range(len(boy)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        return firstName_name + name_1 + boy_name #+ "\t男"

def main():
    random__name = random_name()
    generate__ID = generate_ID(gender=1)
    HB_loanReqNo = loanReqNo()
    HB_creditReqNo = creditReqNo()
    HB_phone = phone()
    hyzllg = Hyzllg(HB_loanReqNo,HB_creditReqNo,random__name,generate__ID,"18390530425","5000","6","6228482089558543378","中国农业银行","17633926705")
    # hyzllg = Hyzllg(HB_loanReqNo,"yy2020082601","陈裕明","421182199509162919","13400121112","5000","6","6214832172362282","中国农业银行","18390530425")
    # hyzllg = Hyzllg(HB_loanReqNo,HB_creditReqNo,"时礼腾","430412198708269819",HB_phone,"5000","6","6214832172362282","中国农业银行","18390530425")


    test_info = f'''
                    姓名：{random__name}
                    身份证号：{generate__ID}
                    手机号：{HB_phone}
                    借款金额:{hyzllg.loanAmount}
                    借款期次:{hyzllg.periods}
                    loanReqNo:{HB_loanReqNo}
                    creditReqNo:{HB_creditReqNo}
                '''
    hyzllg.insure_info()   # 投保信息接口
    Insure_Data_Query = hyzllg.insure_data_query()  # 投保资料查询接口
    hyzllg.insure(Insure_Data_Query[3])   # 投保接口
    hyzllg.credit_granting()  #授信接口
    hyzllg.credit_inquiry()  #授信结果查询
    hyzllg.disburse()    #支用接口
    # hyzllg.disburse_in_query()  #支用查询
    time.sleep(1)
    print(test_info)
    # raw_input("Press <enter>")




if __name__ == '__main__':
        # main()
    for i in range(1):
        main()