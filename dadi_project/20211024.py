import time
from past.builtins import raw_input
import Collect
import yaml


class Hyzllg:
    def __init__(self, **kwargs):
        self.channelCustId = kwargs["channelCustId"]
        self.creditReqNo = kwargs["creditReqNo"]
        self.loanReqNo = kwargs["loanReqNo"]
        self.name = kwargs["name"]
        self.idNo = kwargs["idNo"]
        self.phone = kwargs["phone"]
        self.loanAmount = kwargs["loanAmount"]
        self.repayAmount = kwargs["repayAmount"]
        self.periods = kwargs["periods"]
        self.bankcard = kwargs["bankcard"]
        self.url = kwargs["url"]
        self.custType = kwargs["custType"]


    def credit_granting(self):
        data = {
            "channelCustId": self.channelCustId,
            "creditReqNo": self.creditReqNo,
            "name": self.name,
            "spelling": "ZHANGTIAN",
            "sex": "01",
            "nationality": "中国",
            "nation": "汉族",
            "birthday": "1985/06/02",
            "idType": "00",
            "idNo": self.idNo,
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
            "profession": "11",
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
            "phone": self.phone,
            "email": "email163@qq.com",
            "contacts": [{
                "relation": "00",
                "name": "张三",
                "phoneNo": "15638530000"
            }, {
                "relation": "01",
                "name": "李四",
                "phoneNo": "15638539999"
            }],
            "bankCard": self.bankcard,
            "bankName": "建设银行",
            "bankPhone": self.phone,
            "applyProvince": "110000",
            "applyCity": "110000",
            "applyDistrict": "110101",
            "loanAmount": self.repayAmount,
            "periods": self.periods,
            "purpose": "01",
            "direction": "01",
            "payType": "00",
            "payMerchantNo": "26666",
            "authFlag": "01",
            "deviceDetail": {
                "deviceId": "10-45-5-486",
                "mac": "3a:b6:c6:5d:2e:f9",
                "longitude": "121.551738",
                "latitude": "31.224634",
                "gpsCity": "上海市",
                "ip": "106.14.135.199",
                "ipCity": "上海",
                "os": "android",
                "docDate": "2019/09/12"
            },
            "channelDetail": {
                "citizenshipCheckResult": "1",
                "bankCheckResult": "1",
                "telcoCheckResult": "1",
                "consumeTimes": "1",
                "creditTimes": "1",
                "consumeScene": "1",
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
                "transFlag": "1",
                "custType": self.custType,
                "currLimit": 5000,
                "currRemainLimit": 2000,
                "currLimitOrg": "DD",
                "currLimitStartDate": "2021/05/31",
                "currLimitEndDate": "2021/07/31",
                "currTotalPrice": 28.11,
                "firstLoanFlag": "1",
                "unsettleLoanLimit": 1,
                "settleLoanLimit": 1,
                "lastLoanDate": "2021/04/21",
                "loanAmount": 3000
            }
        }


        url = self.url["credit_granting"]
        title = "**********授信申请！**********"
        requit = Collect.test_api(url,data,title)

        if requit["result"] == True:
            creditApplyNo = requit["data"]["body"]["creditApplyNo"]
            print("授信接口调用成功！")
            if requit["data"]["body"]["status"] == "01":
                print("授信受理成功，处理中！")
            else:
                print("授信受理失败！")
                raw_input("Press <enter>")

        else:
            print("未知异常！")
            raw_input("Press <enter>")
        return creditApplyNo

    def credit_inquiry(self, creditApplyNo):
        hhh = 0
        data = {
            "channelCustId": self.channelCustId,
            "creditReqNo": self.creditReqNo,
            "creditApplyNo": creditApplyNo
        }

        time.sleep(2)
        n = False
        while hhh < 30:
            url = self.url["credit_inquiry"]
            title = "**********授信结果查询！**********"
            requit = Collect.test_api(url, data, title)
            print("授信查询接口调用成功！")
            try:
                if requit["data"]["body"]["status"] == "01":
                    print("授信通过！")
                    n = True
                    break
                elif requit["data"]["body"]["status"] == "00":
                    print("授信中！")
                    time.sleep(3)
                    hhh += 1
                    continue
                else:
                    print("授信失败！")
                    exit()
            except KeyError:
                print("甜橙授信查询接口响应异常！")
                exit()



        if hhh >= 16:
            print("甜橙授信时间过长！可能由于授信挡板问题，结束程序！")
            raw_input("Press <enter>")

        return n

    def disburse_trial(self, capitalCode):
        data = {
            "channelCustId": self.channelCustId,
            "periods": self.periods,
            "loanAmount": self.loanAmount
        }

        while True:
            url = self.url["disburse_trial"]
            title = "**********支用试算！**********"
            requit = Collect.test_api(url, data, title)
            if requit["result"] == True:
                print(f'本次试算资方为：{requit["data"]["body"]["capitalCode"]}')
                if requit["data"]["body"]["status"] == "01" and requit["data"]["body"]["capitalCode"] == capitalCode:
                    print("支用试算成功！")
                    break
                else:
                    time.sleep(3)
                    continue
            else:
                print("未知异常！")
                raw_input("Press <enter>")

    def disburse(self, capitalCode):
        data = {
            "channelCustId": self.channelCustId,
            "loanReqNo": self.loanReqNo,
            "creditReqNo": self.creditReqNo,
            "loanAmount": self.loanAmount,
            "periods": self.periods,
            "purpose": "01",
            "bankCard": self.bankcard,
            "bankCode": "308584000013",
            "bankName": "建设银行",
            "bankPhone": self.phone,
            "longitude": "121.551738",
            "latitude": "31.224634",
            "ip": "192.168.1.2",
            "capitalCode": capitalCode,
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
                "transFlag": "1",
                "custType": self.custType,
                "currLimit": 5000,
                "currRemainLimit": 2000,
                "currLimitOrg": "DD",
                "currLimitStartDate": "2021/05/31",
                "currLimitEndDate": "2021/07/31",
                "currTotalPrice": 28.11,
                "firstLoanFlag": "1",
                "unsettleLoanLimit": 1,
                "settleLoanLimit": 1,
                "lastLoanDate": "2021/04/21",
                "loanAmount": 3000
            }
        }
        url = self.url["disburse"]
        title = "**********支用接口！**********"
        requit = Collect.test_api(url, data, title)
        if requit["result"] == True:
            print("支用接口调用成功！")
            if requit["data"]["body"]["status"] == "01":
                print("受理成功，处理中!")
            else:
                print("受理失败")
                raw_input("Press <enter>")
        else:
            print("未知异常！")
            raw_input("Press <enter>")

    def disburse_in_query(self, loanReqNo):
        data = {
            "channelCustId": self.channelCustId,
            "creditReqNo": loanReqNo,
            "loanReqNo": self.creditReqNo
        }

        time.sleep(5)
        while True:
            url = self.url["disburse_in_query"]
            title = "**********支用结果查询！**********"
            requit = Collect.test_api(url, data, title)
            if requit["result"] == True:
                print("支用结果查询接口调用成功！")
                if requit["data"]["body"]["status"] == "01":
                    print("支用成功")
                    break
                elif requit["data"]["body"]["status"] == "00":
                    print("处理中！")
                else:
                    print("支用失败！")
                    raw_input("Press <enter>")
            else:
                print("未知异常！")
                raw_input("Press <enter>")
            time.sleep(3)



def tc_main(number,repayAmount,loanAmount,periods,custType,capitalCode,environment,loan_datetime=time.strftime("%Y-%m-%d")):
    #获取配置信息
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    res_url = get_yaml_data('./setting/Config.yaml')["api_url_tc"]
    abc=[]
    for i in range(number):
        # 指定姓名身份证手机号时使用
        # random_name = "张八"
        # generate__ID = "542128196305226980"
        # ORANGE_phone = "13800138001"
        # ORANGE_bankcard = "5555666677778889"
        random_name = Collect.random_name()
        generate__ID = Collect.id_card().generate_ID()
        ORANGE_phone = Collect.phone()
        ORANGE_bankcard = Collect.bankcard()

        channelCustId = Collect.random_number_reqno()
        creditReqNo = Collect.random_number_reqno()
        loanReqNo = Collect.random_number_reqno()
        if environment == "SIT":
            hyzllg = Hyzllg(channelCustId=channelCustId,
                            creditReqNo=creditReqNo,
                            loanReqNo = loanReqNo,
                            name = random_name,
                            idNo = generate__ID,
                            phone = ORANGE_phone,
                            repayAmount = repayAmount,
                            loanAmount = loanAmount,
                            periods = periods,
                            bankcard = ORANGE_bankcard,
                            url = res_url["sit_url_tc"],
                            custType = custType)
            credit = hyzllg.credit_granting()
            abc.append(
                {"channelCustId" : channelCustId,
                 "creditReqNo" : creditReqNo,
                 "loanReqNo" : loanReqNo,
                 "name" : random_name,
                 "idNo" : generate__ID,
                 "phone" : ORANGE_phone,
                 "repayAmount" : repayAmount,
                 "loanAmount" : loanAmount,
                 "periods" : periods,
                 "bankcard" : ORANGE_bankcard,
                 "url" : res_url["sit_url_tc"],
                 "credit" : credit,
                 "custType" : custType})
        elif environment == "UAT":
            hyzllg = Hyzllg(channelCustId=channelCustId,
                            creditReqNo=creditReqNo,
                            loanReqNo = loanReqNo,
                            name = random_name,
                            idNo = generate__ID,
                            phone = ORANGE_phone,
                            repayAmount = repayAmount,
                            loanAmount = loanAmount,
                            periods = periods,
                            bankcard = ORANGE_bankcard,
                            url = res_url["uat_url_tc"],
                            custType = custType)
            credit = hyzllg.credit_granting()
            abc.append(
                {"channelCustId" : channelCustId,
                 "creditReqNo" : creditReqNo,
                 "loanReqNo" : loanReqNo,
                 "name" : random_name,
                 "idNo" : generate__ID,
                 "phone" : ORANGE_phone,
                 "repayAmount" : repayAmount,
                 "loanAmount" : loanAmount,
                 "periods" : periods,
                 "bankcard" : ORANGE_bankcard,
                 "url" : res_url["uat_url_tc"],
                 "credit" : credit,
                 "custType" : custType})
        elif environment == "DEV":
            hyzllg = Hyzllg(channelCustId=channelCustId,
                            creditReqNo=creditReqNo,
                            loanReqNo = loanReqNo,
                            name = random_name,
                            idNo = generate__ID,
                            phone = ORANGE_phone,
                            repayAmount = repayAmount,
                            loanAmount = loanAmount,
                            periods = periods,
                            bankcard = ORANGE_bankcard,
                            url = res_url["dev_url_tc"],
                            custType = custType)
            credit = hyzllg.credit_granting()
            abc.append(
                {"channelCustId" : channelCustId,
                 "creditReqNo" : creditReqNo,
                 "loanReqNo" : loanReqNo,
                 "name" : random_name,
                 "idNo" : generate__ID,
                 "phone" : ORANGE_phone,
                 "repayAmount" : repayAmount,
                 "loanAmount" : loanAmount,
                 "periods" : periods,
                 "bankcard" : ORANGE_bankcard,
                 "url" : res_url["dev_url_tc"],
                 "credit" : credit,
                 "custType" : custType})
        else:
            print("........")

    nnn = False
    n = 0
    # input("输入")
    while len(abc):
        for i in abc:
            # （参数1：apply/query；参数2：流水号；参数3：放款时间，格式y-m-d)
            if capitalCode == "LJBANK":
                Collect.start_lj_mock()
                ljreqno = Collect.random_number_reqno()
                Collect.update_lj_mock("apply", ljreqno, loan_datetime)
                Collect.update_lj_mock("query", ljreqno, loan_datetime)
            hyzllg = Hyzllg(channelCustId=i['channelCustId'],
                            creditReqNo=i['creditReqNo'],
                            loanReqNo = i['loanReqNo'],
                            name = i['name'],
                            idNo = i['idNo'],
                            phone = i['phone'],
                            repayAmount = i['repayAmount'],
                            loanAmount = i['loanAmount'],
                            periods =i['periods'],
                            bankcard = i['bankcard'],
                            url = i['url'],
                            custType = i['custType'])
            if hyzllg.credit_inquiry(i['credit']):
                hyzllg.disburse_trial(capitalCode)
                hyzllg.disburse(capitalCode)
                # Python_crawler.disburse_in_query(ORANGE_serial_number[2])
                abc.remove(i)
                nnn = True
            n += 1
            if n > 30 and nnn == False:
                raw_input("Press <enter>")
            test_info = f'''
                    姓名：{i['name']}
                    身份证号：{i['idNo']}
                    手机号：{i['phone']}
                    借款金额:{i['loanAmount']}
                    借款期次:{i['periods']}
                    channelCustId：{i['channelCustId']}
                    creditReqNo：{i['creditReqNo']}
                    loanReqNo:{i['loanReqNo']}
                    '''
            print(test_info)

def main():
    #环境（sit,uat,dev）
    environment = "uat"
    #走数据笔数
    number = 1
    #放款金额
    repayAmount = 5000
    # 借款金额
    loanAmount = 2000
    # 期数
    periods = "3"
    # 客户类型,0是新用户，1是存量活跃，2是存量静默
    custType = "0"
    # 资方编码 富邦银行：FBBANK 龙江银行：LJBANK
    capitalCode = "FBBANK"
    #龙江放款mock，设定放款日期
    # loan_datetime = "2021-09-16"
    tc_main(number,repayAmount,loanAmount,periods,custType,capitalCode,environment.upper())

if __name__ == '__main__':
    main()





