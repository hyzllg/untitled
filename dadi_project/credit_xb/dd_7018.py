import os
import re as res
import time
import yaml
from utils import generate_customer_info,api_request,my_log


class Hyzllg:
    def __init__(self, **kwargs):
        self.loanReqNo = kwargs["loanReqNo"]
        self.creditReqNo = kwargs["creditReqNo"]
        self.name = kwargs["name"]
        self.idNo = kwargs["idNo"]
        self.phone = kwargs["phone"]
        self.loanAmount = kwargs["loanAmount"]
        self.periods = kwargs["periods"]
        self.bankCard = kwargs["bankCard"]
        self.url = kwargs["url"]
        self.res_data = kwargs["res_data"]
        self.custGrde = kwargs["custGrde"]
        self.log = my_log.Log()

    def insure_info(self):
        data = self.res_data["insure_info"]
        data["insuranceNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        data["custGrde"] = self.custGrde
        url = self.url["insure_info"]
        self.log.info("投保信息接口")
        self.log.info(url)
        requit = api_request.request_api().test_api("post", url, data)
        try:
            if requit["result"] == True:
                a = requit["data"]["insurUrl"]
                b = res.search("lp=(.*)", a)
                c = b.group()[3:]
                self.log.info("投保信息接口成功！")
            else:
                self.log.error("投保信息接口失败！")
                exit()
        except KeyError:
            self.log.error("拍拍贷投保信息接口响应异常！")
            exit()
        return c

    def insure_data_query(self, token):
        data = self.res_data["insure_data_query"]
        data["loanReqNo"] = self.loanReqNo
        data["token"] = token
        url = self.url['insure_data_query']
        self.log.info("投保资料查询接口")
        self.log.info(url)
        requit = api_request.request_api().test_api("post", url, data)
        try:
            if requit["result"] == True:
                self.log.info("投保资料查询成功！")
            else:
                self.log.error("投保资料查询失败！")
                exit()
        except KeyError:
            self.log.error("拍拍贷投保资料查询接口响应异常！")
            exit()

        return requit["data"]["insurantName"],requit["data"]["premiumRate"]

    def insure(self, insurantName, premiumRate ):
        data = self.res_data["insure"]
        data["loanReqNo"] = self.loanReqNo
        data["insReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        data["premiumRate"] = premiumRate
        data["insurantName"] = insurantName
        url = self.url['insure']
        self.log.info("投保接口")
        self.log.info(url)
        requit = api_request.request_api().test_api("post", url, data)
        try:
            if requit["result"] == True:
                try:
                    if requit["data"]["message"]:
                        self.log.error("受理失败")
                        exit()
                except BaseException as e:
                    if requit["data"]["status"] == '01':
                        self.log.info("已受理，处理中！")
            else:
                self.log.error("未知异常！")
                exit()
        except KeyError:
            self.log.error("拍拍贷投保接口响应异常！")
            exit()


    def credit_granting(self):
        data = self.res_data['credit_granting']
        data["insuranceNo"] = self.loanReqNo
        data["creditReqNo"] = self.creditReqNo
        data["name"] = self.name
        data["phone"] = self.phone
        data["idNo"] = self.idNo
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankCard
        data["bankPhone"] = self.phone
        data["docDate"] = time.strftime("%Y/%m/%d")
        data["channelDetail"]["custGrde"] = self.custGrde
        url = self.url['credit_granting']
        self.log.info("授信接口")
        self.log.info(url)
        requit = api_request.request_api().test_api("post", url, data)
        try:
            if requit["result"] == True:
                try:

                    if requit["data"]["status"] == "01":
                        self.log.info("授信受理成功，处理中！")
                    elif requit["data"]["status"] == "00":
                        print(requit)
                        self.log.error("受理失败！")
                        exit()
                except BaseException as e:
                    self.log.error("未知异常！")
                    exit()
            else:
                self.log.error("未知异常！")
                exit()
        except KeyError:
            self.log.error("拍拍贷授信接口响应异常！")
            exit()

    def credit_inquiry(self):
        data = self.res_data["credit_inquiry"]
        data["creditReqNo"] = self.creditReqNo
        number = 0
        n = False
        while number <= 30:
            url = self.url['credit_inquiry']
            self.log.info("授信结果查询")
            self.log.info(url)
            requit = api_request.request_api().test_api("post", url, data)
            try:
                if requit["result"] == True:
                    self.log.info("授信查询接口调用成功！")
                    try:
                        if requit["data"]["status"] == "01":
                            self.log.info("授信通过！")
                            n = True
                            break
                        elif requit["data"]["status"] == "00":
                            self.log.info("授信中！")
                            time.sleep(3)
                        else:
                            self.log.error("授信失败！")
                            exit()
                    except BaseException as e:
                        self.log.error("未知异常！")
                        exit()

                else:
                    self.log.error("未知异常！")
                    exit()
            except KeyError:
                self.log.error("拍拍贷授信结果查询接口响应异常！")
                exit()
            number += 1
        if number >= 10:
            self.log.error("拍拍贷授信时间过长！可能由于授信挡板问题，结束程序！")
            exit()

        return n

    def disburse(self):
        data = self.res_data['disburse']
        data["creditReqNo"] = self.creditReqNo
        data["loanReqNo"] = self.loanReqNo
        url = self.url['disburse']
        self.log.info("支用接口")
        self.log.info(url)
        requit = api_request.request_api().test_api("post", url, data)
        try:
            if requit["result"] == True:
                if requit["data"]["status"] == "01":
                    self.log.info("支用受理成功，处理中！")
                elif requit["data"]["status"] == "00":
                    self.log.error("支用受理失败！")
                    exit()
            else:
                self.log.error("未知异常！")
                exit()
        except KeyError:
            self.log.error("拍拍贷支用接口响应异常！")
            exit()

    def disburse_in_query(self):
        data = self.res_data["disburse_in_query"]
        data["creditReqNo"] = self.creditReqNo
        data["loanReqNo"] = self.loanReqNo
        while True:
            url = self.url['disburse_in_query']
            self.log.info("支用结果查询")
            self.log.info(url)
            requit = api_request.request_api().test_api("post", url, data)
            try:
                if requit["result"] == True:
                    self.log.info("支用查询接口调用成功！")
                    if requit["data"]["status"] == "01":
                        self.log.info("支用通过！")
                        break
                    elif requit["data"]["status"] == "00":
                        self.log.info("支用中！")
                    else:
                        self.log.error("支用失败！")
                        exit()

                else:
                    self.log.error("未知异常！")
                    exit()
            except KeyError:
                self.log.error("拍拍贷支用结果接口响应异常！")
                exit()


def pp_main(environment,number,loanAmount,periods,custGrde):
    #获取配置信息
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    path = os.path.dirname(os.path.dirname(__file__))
    res_url = get_yaml_data(f'{path}/conf/url_res/api_url_pp.yaml')
    res_data = get_yaml_data(f'{path}/conf/loan_res/pp_res_data.yaml')
    abc = []
    for i in range(number):
        loanReqNo = generate_customer_info.customer().reqno(66)
        creditReqNo = generate_customer_info.customer().reqno(88)

        idNo = generate_customer_info.customer().idNo()
        name = generate_customer_info.customer().name()
        phone = generate_customer_info.customer().phone()
        bankcard = generate_customer_info.customer().bankcard()
        # 指定姓名身份证手机号时使用
        # name = "乔贝义"
        # idNo = "320481199403069017"
        # phone = "16610277481"
        # bankcard = "6200582541215452181"
        if environment == "SIT":
            hyzllg = Hyzllg(loanReqNo=loanReqNo,
                            creditReqNo=creditReqNo,
                            name=name,
                            idNo=idNo,
                            phone=phone,
                            loanAmount=loanAmount,
                            periods=periods,
                            bankCard=bankcard,
                            url=res_url["sit_url_pp"],
                            res_data=res_data,
                            custGrde=custGrde)
            insure = hyzllg.insure_info()  # 投保信息接口
            Insure_Data_Query = hyzllg.insure_data_query(insure)  # 投保资料查询接口
            hyzllg.insure(Insure_Data_Query[0],Insure_Data_Query[1])  # 投保接口
            hyzllg.credit_granting()  # 授信接口
            abc.append(
                {"creditReqNo" : creditReqNo,
                 "loanReqNo" : loanReqNo,
                 "name" : name,
                 "idNo" : idNo,
                 "phone" : phone,
                 "loanAmount" : loanAmount,
                 "periods" : periods,
                 "bankcard" : bankcard,
                 "url" : res_url["sit_url_pp"],
                 "res_data" : res_data,
                 "custGrde" : custGrde})
        elif environment == "UAT":
            hyzllg = Hyzllg(loanReqNo=loanReqNo,
                            creditReqNo=creditReqNo,
                            name=name,
                            idNo=idNo,
                            phone=phone,
                            loanAmount=loanAmount,
                            periods=periods,
                            bankCard=bankcard,
                            url=res_url["uat_url_pp"],
                            res_data=res_data,
                            custGrde=custGrde)
            insure = hyzllg.insure_info()  # 投保信息接口
            Insure_Data_Query = hyzllg.insure_data_query(insure)  # 投保资料查询接口
            hyzllg.insure(Insure_Data_Query[0],Insure_Data_Query[1])  # 投保接口
            hyzllg.credit_granting()  # 授信接口
            abc.append(
                {"creditReqNo" : creditReqNo,
                 "loanReqNo" : loanReqNo,
                 "name" : name,
                 "idNo" : idNo,
                 "phone" : phone,
                 "loanAmount" : loanAmount,
                 "periods" : periods,
                 "bankcard" : bankcard,
                 "url" : res_url["uat_url_pp"],
                 "res_data" : res_data,
                 "custGrde" : custGrde})
        elif environment == "DEV":
            hyzllg = Hyzllg(loanReqNo=loanReqNo,
                            creditReqNo=creditReqNo,
                            name=name,
                            idNo=idNo,
                            phone=phone,
                            loanAmount=loanAmount,
                            periods=periods,
                            bankCard=bankcard,
                            url=res_url["dev_url_pp"],
                            res_data=res_data,
                            custGrde=custGrde)
            insure = hyzllg.insure_info()  # 投保信息接口
            Insure_Data_Query = hyzllg.insure_data_query(insure)  # 投保资料查询接口
            hyzllg.insure(Insure_Data_Query[0],Insure_Data_Query[1])  # 投保接口
            hyzllg.credit_granting()  # 授信接口
            abc.append(
                {"creditReqNo" : creditReqNo,
                 "loanReqNo" : loanReqNo,
                 "name" : name,
                 "idNo" : idNo,
                 "phone" : phone,
                 "loanAmount" : loanAmount,
                 "periods" : periods,
                 "bankcard" : bankcard,
                 "url" : res_url["dev_url_pp"],
                 "res_data" : res_data,
                 "custGrde" : custGrde})
        else:
            print("........")

    time.sleep(5)
    # a = input("aaa")
    nnn = False
    n = 0
    while len(abc):
        for i in abc:
            hyzllg = Hyzllg(loanReqNo=i["loanReqNo"],
                            creditReqNo=i["creditReqNo"],
                            name=i["name"],
                            idNo=i["idNo"],
                            phone=i["phone"],
                            loanAmount=i["loanAmount"],
                            periods=i["periods"],
                            bankCard=i["bankcard"],
                            url=i["url"],
                            res_data=i["res_data"],
                            custGrde=i["custGrde"]
                            )
            if hyzllg.credit_inquiry():
                hyzllg.disburse()
                abc.remove(i)
                nnn = True
            n += 1
            if n > 30 and nnn == False:
                exit()
            test_info = f'''
                            姓名：{i["name"]}
                            身份证号：{i["idNo"]}
                            手机号：{i["phone"]}
                            借款金额:{i["loanAmount"]}
                            借款期次:{i["periods"]}
                            loanReqNo:{i["loanReqNo"]}
                            creditReqNo:{i["creditReqNo"]}
                        '''
            log = my_log.Log()
            log.info(test_info)



def main():
    #环境（sit,uat,dev）
    environment = "sit"
    #走数据笔数
    number = 1
    # 借款金额
    loanAmount = 3000
    # 期数
    periods = "6"
    # 客户等级上下限
    custGrde = 20
    pp_main(environment.upper(),number,loanAmount,periods,custGrde)

if __name__ == '__main__':
    main()
