import random
import requests
import json
import threading
import time
import re
import os
from past.builtins import raw_input


class Hyzllg:
    def __init__(self,channelCustId,creditReqNo,name,idNo,phone,loanAmount,periods,bankcard):
        self.channelCustId = channelCustId
        self.creditReqNo = creditReqNo
        self.name = name
        self.idNo = idNo
        self.phone = phone
        self.loanAmount = loanAmount
        self.periods = periods
        self.bankcard = bankcard

    def wrapper(func):
        def inner(*args,**kwargs):
            s = func(*args,**kwargs)
            with open(os.path.join(os.path.expanduser("~"), 'Desktop')+"\ORANGE.log", 'a+', encoding='utf-8') as hyzllg:
                hyzllg.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s[0]} {s[1]} {s[2]}")

        return inner
    @wrapper
    def credit_granting(self):

        url = 'http://10.1.14.117:27405/channel/TEST/TCJQ/CREDIT_GRANTING'
        data = {
            "channelCustId": "20200612886881020",
            "creditReqNo": "20200612668661020",
            "name": "荆宗",
            "spelling": "ZHANGTIAN",
            "sex": "01",
            "nationality": "中国",
            "nation": "汉族",
            "birthday": "1985/06/02",
            "idType": "00",
            "idNo": "51343619900612877X",
            "idStartDate": "2016/01/18",
            "idEndDate": "2036/01/18",
            "idOffice": "北京市东城区",
            "marriage": "01",
            "children": "00",
            "supplyPeople": 3,
            "house": "00",
            "addProvince": "110000",
            "addCity": "110000",
            "addDistrict": "110101",
            "addDetail": "东大街东大院",
            "industry": "C",
            "profession": "04",
            "workplaceName": "AAA单位",
            "workTel": "13162314539",
            "workProvince": "110000",
            "workCity": "110000",
            "workDistrict": "110101",
            "workDetailAdd": "西大街西大院",
            "workAge": 8,
            "income": "03",
            "education": "06",
            "school": "北京大学",
            "phone": "16606124020",
            "email":"email163@qq.com",
            "contacts": [{
                "relation": "00",
                "name": "张三",
                "phoneNo": "15638537485"
            },{
                "relation": "01",
                "name": "李四",
                "phoneNo": "15638537486"
             }],
            "bankCard": "6214852127765553",
            "bankName": "建设银行",
            "bankPhone": "15638537487",
            "applyProvince": "110000",
            "applyCity": "110000",
            "applyDistrict": "110101",
            "loanAmount": "5000.00",
            "periods": 6,
            "purpose": "01",
            "direction": "01",
            "payType": "00",
            "payMerchantNo": "26666",
            "authFlag": "01",
            "deviceDetail": {
                "deviceId": "10-45-5-486",
                "mac": "sjdfsjdfhskldjf ",
                "longitude": "121.551738",
                "latitude": "31.224634",
                "gpsCity": "上海市",
                "ip": "106.14.135.199",
                "ipCity": "上海",
                "os": "android",
                "docDate": "2019/09/12"
            },
            "channelDetail": {
                    "citizenshipCheckResult":"1",
                    "bankCheckResult":"1",
                    "telcoCheckResult":"1",
                    "consumeTimes":"1",
                    "creditTimes":"1",
                    "consumeScene":"1",
                    "frontId": "11",
                    "reverseId": "11",
                    "faceId": "11",
                    "woolFlag": "1",
                    "phoneFlag": "1",
                    "phoneTelco": "1",
                    "compScore": "650",
                    "repayAbilityScore": "650",
                    "comsAmount": "1",
                    "finAmount": "1",
                    "redPacket": "1",
                    "phoneAreaName": "上海市",
                    "modelScore": "650",
                    "whiteListFlag": "0",
                    "sugAmount": "3000.00",
                    "sugBasis": "2",
                    "loanGrade": "A",
                    "registerTime": "1",
                    "realNameFlag": "1",
                    "realNameGrade": "1",
                    "transFlag": "1"
              }
        }
        data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = self.creditReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankcard
        data["bankPhone"] = self.phone

        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********授信申请！**********"
        print(a)
        print(f"请求报文：{data}")
        # time.sleep(2)
        re = requests.post(url,data=json.dumps(data),headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            print("授信接口调用成功！")
            if requit["data"]["body"]["status"] == "01":
                print(f"响应报文：{requit}")
                print("授信受理成功，处理中！")
            else:
                print("授信受理失败！")
                if requit["data"]["message"]:
                    print(f'errormsg:{requit["data"]["message"]}')
                    raw_input("Press <enter>")

        else:
            print("授信接口调用异常！")
            raw_input("Press <enter>")
        return url, a, requit

    @wrapper
    def credit_inquiry(self):
        url = 'http://10.1.14.117:27405/channel/TEST/TCJQ/CREDIT_INQUIRY'
        data = {
                "channelCustId": "20200612886881021",
                "creditReqNo": "20200612668661021"
            }
        data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = self.creditReqNo
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

        }

        while True:
            a = "**********授信结果查询！**********"
            print(a)
            print(f"请求报文：{data}")
            time.sleep(5)
            re = requests.post(url, data=json.dumps(data), headers=headers)
            requit = re.json()
            requit["data"] = eval(requit["data"])
            if re.status_code == 200:
                print("授信查询接口调用成功！")
                try:
                    if requit["data"]["body"]["status"]=="01":
                        print(f"响应报文：{requit}")
                        print("授信通过！")
                        break
                    elif requit["data"]["body"]["status"]=="00":
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
        return url, a, requit

    @wrapper
    def disburse_trial(self,capitalCode):
        url = 'http://10.1.14.117:27405/channel/TEST/TCJQ/DISBURSE_TRIAL'
        data = {
            "channelCustId": "20200612886881021",
            "periods": 6,
            "loanAmount": "1000.00"
        }
        data["channelCustId"] = self.channelCustId
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用试算！**********"
        print(a)
        print(f"请求报文：{data}")
        res = requests.post(url,data=json.dumps(data),headers=headers)
        requit = res.json()
        requit["data"] = eval(requit["data"])
        time.sleep(2)
        while True:
            if res.status_code == 200:
                print(f'本次试算资方为：{requit["data"]["body"]["capitalCode"]}')
                if requit["data"]["body"]["status"]=="01" and requit["data"]["body"]["capitalCode"]==capitalCode:
                    print(f"响应报文：{requit}")
                    print("支用试算成功！")
                    break
                else:
                    time.sleep(3)
                    continue

            else:
                print("支用试算接口调用异常！")
                raw_input("Press <enter>")
        return url, a, requit

    @wrapper
    def disburse(self,loanReqNo,capitalCode):
        url = 'http://10.1.14.117:27405/channel/TEST/TCJQ/DISBURSE'
        data = {
                "channelCustId": "20200612886881021",
                "loanReqNo": "202006128866881022",
                "creditReqNo": "20200612668661021",
                "loanAmount": "1000.00",
                "periods": 6,
                "purpose": "01",
                "bankCard": "6214852127765553",
                "bankCode": "308584000013",
                "bankName": "建设银行",
                "bankPhone": "13800000004",
                "longitude": "121.551738",
                "latitude": "31.224634",
                "ip": "192.168.1.2",
                "capitalCode":"HNTRUST",
                "channelDetail": {
                    "woolFlag": "1",
                    "phoneFlag": "1",
                    "phoneTelco": "1",
                    "compScore": "80",
                    "repayAbilityScore": "80",
                    "comsAmount": "4",
                    "finAmount": "2",
                    "redPacket": "2",
                    "phoneAreaName": "上海市",
                    "modelScore": "80",
                    "whiteListFlag": "0",
                    "loanGrade": "A",
                    "registerTime": "2",
                    "realNameFlag": "1",
                    "realNameGrade": "1",
                    "transFlag": "1"
                }
                    }
        data["channelCustId"] = self.channelCustId
        data["loanReqNo"] = loanReqNo
        data["creditReqNo"] = self.creditReqNo
        data["capitalCode"] = capitalCode
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankcard
        data["bankPhone"] = self.phone
        print(data)
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用接口！**********"
        print(a)
        print(f"请求报文：{data}")
        time.sleep(1)
        re = requests.post(url,data=json.dumps(data),headers=headers)
        requit = re.json()
        requit["data"] = eval(requit["data"])
        if re.status_code == 200:
            print("支用接口调用成功！")
            if requit["data"]["body"]["status"]=="01":
                print(f"响应报文：{requit}")
                print("受理成功，处理中!")
            else:
                print("受理失败")
                if requit["data"]["message"]:
                    print(f'errormsg:{requit["data"]["message"]}')
                    raw_input("Press <enter>")
        else:
            print("支用接口调用异常！")
            raw_input("Press <enter>")

        return url, a, requit

    @wrapper
    def disburse_in_query(self,loanReqNo):
        url = 'http://10.1.14.117:27405/channel/TEST/TCJQ/DISBURSE_IN_QUERY'
        data = {
                "channelCustId":"20200612886881021",
                "creditReqNo":"20200612668661021",
                "loanReqNo":"202006128866881022"
        }
        data["channelCustId"] = self.channelCustId
        data["loanReqNo"] = loanReqNo
        data["creditReqNo"] = self.creditReqNo
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "Host":"10.1.14.106:27405",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********支用结果查询！**********"
        print(a)
        print(f"请求报文：{data}")
        time.sleep(10)
        while True:
            re = requests.post(url, data=json.dumps(data), headers=headers)
            requit = re.json()
            requit["data"] = eval(requit["data"])
            if re.status_code == 200:
                print("支用结果查询接口调用成功！")
                if requit["data"]["body"]["status"]=="01":
                    print(f"响应报文：{requit}")
                    print("支用成功")
                    break
                elif requit["data"]["body"]["status"]=="00":
                    print("处理中！")
                else:
                    print("支用失败！")
                    if requit["data"]["message"]:
                        print(f'errormsg:{requit["data"]["message"]}')
                        raw_input("Press <enter>")
            else:
                print("支用结果查询接口调用异常！")
                raw_input("Press <enter>")
            time.sleep(10)
        return url, a, requit

def serial_number():
    a = str(random.randint(1, 1000))
    b = time.strftime("%Y%m%d%H%M%S")
    channelCustId = b + '68' + a
    creditReqNo = b + '86' + a
    loanReqNo = b + '686' + a
    return channelCustId,creditReqNo,loanReqNo

def phone():
    a = str(random.randint(1000,10000))
    b = time.strftime("%m%d")
    phone = "166"+b+a
    return phone

def bankcard():
    a = str(random.randint(1000,10000))
    b = time.strftime("%m%d%H%M%S")
    bankcard = '621083' + b
    return bankcard


def name_idno():
    url = f'http://www.xiaogongju.org/index.php/index/id.html/id/513224/year/1990/month/{time.strftime("%m")}/day/{time.strftime("%d")}/sex/%E7%94%B7'

    headers = {
        "Content-Type":"text/html;charset=utf-8",
        "Host":"www.xiaogongju.org",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    print("*********爬取姓名身份证信息*********")
    print(url)
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
    while True:
        hlp = input("选择资方(1：徽商，2：微众)：")
        # hlp = "2"
        if hlp == "1":
            hlp = 'HNTRUST'
            break
        elif hlp == "2":
            hlp = 'FBBANK'
            break
        else:
            print("输入错误!")

    random__name = random_name()
    generate__ID = generate_ID(gender=1)
    ORANGE_phone = phone()
    ORANGE_serial_number = serial_number()
    ORANGE_bankcard = bankcard()
    hyzllg = Hyzllg(ORANGE_serial_number[0],ORANGE_serial_number[1], random__name, generate__ID,ORANGE_phone,"5000.00","12",ORANGE_bankcard)
    test_info = f'''
            姓名：{random__name}
            身份证号：{generate__ID}
            手机号：{ORANGE_phone}
            借款金额:{hyzllg.loanAmount}
            借款期次:{hyzllg.periods}
            channelCustId：{ORANGE_serial_number[0]}
            creditReqNo：{ORANGE_serial_number[1]}
            loanReqNo:{ORANGE_serial_number[2]}
            '''
    hyzllg.credit_granting()
    hyzllg.credit_inquiry()
    capitalCode_ = hyzllg.disburse_trial(hlp)
    hyzllg.disburse(ORANGE_serial_number[2],hlp)
    # hyzllg.disburse_in_query(ORANGE_serial_number[2])
    time.sleep(1)
    print(test_info)
    raw_input("Press <enter>")



if __name__ == '__main__':
    main()