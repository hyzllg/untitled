import cx_Oracle
import json
import os
import time
import re as res
import yaml
import requests
from past.builtins import raw_input
import Collect


class Hyzllg:
    def __init__(self, **kwargs):
        self.loanReqNo = kwargs["loanReqNo"]
        self.name = kwargs["name"]
        self.idNo = kwargs["idNo"]
        self.phone = kwargs["phone"]
        self.loanAmount = kwargs["loanAmount"]
        self.periods = kwargs["periods"]
        self.bankcard = kwargs["bankcard"]
        self.url = kwargs["url"]
        self.res_data = kwargs["res_data"]
        self.discountRate = kwargs["discountRate"]
        self.custGrde = kwargs["custGrde"]


    def insure_info(self):
        data = self.res_data["insure_info"]
        data["loanReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        data["discountRate"] = self.discountRate
        data["custGrde"] = self.custGrde
        url = self.url["insure_info"]
        print("**********投保信息接口**********")
        requit = Collect.test_api(url,data)
        try:
            if requit["result"] == True:
                print("投保信息接口成功！")
                a = requit["data"]["insurAgencyUrl"]
                b = res.search("lp=(.*)", a)
                c = b.group()[3:]
            else:
                print("投保信息接口失败！")
                exit()
        except KeyError:
            print("还呗投保信息接口响应异常！")
            exit()
        return c

    def insure_data_query(self, token):
        data = self.res_data["insure_data_query"]
        data["loanReqNo"] = self.loanReqNo
        data["token"] = token
        url = self.url['insure_data_query']
        print("**********投保资料查询接口**********")
        requit = Collect.test_api(url,data)
        try:
            if requit["result"] == True:
                print("投保资料查询成功！")
            else:
                print("投保资料查询失败！")
                exit()
        except KeyError:
            print("还呗投保资料查询接口响应异常！")
            exit()
        return requit["data"]["premiumRate"]

    def insure(self, a):
        data = self.res_data["insure"]
        data["loanReqNo"] = self.loanReqNo
        data["insReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["amount"] = self.loanAmount
        data["periods"] = self.periods
        data["premiumRate"] = a
        url = self.url['insure']
        print("**********投保接口**********")
        requit = Collect.test_api(url,data)
        try:
            if requit["result"] == True:
                try:
                    if requit["data"]["message"]:
                        print("受理失败")
                        raw_input("Press <enter>")
                except BaseException as e:
                    if requit["data"]["status"] == '01':
                        print("已受理，处理中！")
            else:
                print("未知异常！")
                exit()
        except KeyError:
            print("还呗投保接口响应异常！")
            exit()
        return requit

    def disburse(self):
        data = self.res_data["disburse"]
        data["loanReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["phone"] = self.phone
        data["idNo"] = self.idNo
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankcard
        data["bankPhone"] = self.phone
        data["discountRate"] = self.discountRate
        data["channelDetail"]["custGrde"] = self.custGrde
        url = self.url['disburse']
        print("**********支用接口**********")
        requit = Collect.test_api(url,data)
        try:
            if requit["result"] == True:
                try:

                    if requit["data"]["status"] == "01":
                        print("支用受理成功，处理中！")
                    elif requit["data"]["status"] == "00":
                        print("受理失败！")
                        exit()
                except BaseException as e:
                    print("未知异常！")
                    exit()
            else:
                print("未知异常！")
                exit()
        except KeyError:
            print("还呗支用接口响应异常！")
            exit()


def hb_main(environment,number,loanAmount,periods,custGrde,discountRate):
    #获取配置信息
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    res_url = get_yaml_data('./setting/Config.yaml')["api_url_hb"]
    res_data = get_yaml_data('./setting/request_data.yaml')["hb_res_data"]
    for i in range(number):
        HB_loanReqNo = Collect.random_number_reqno()
        random__name = Collect.random_name()
        generate__ID = Collect.id_card().generate_ID()
        HB_phone = Collect.phone()
        HB_bankcard = Collect.bankcard()
        # 指定姓名身份证手机号时使用
        # random__name = "张八"
        # generate__ID = "542128196305226980"
        # HB_phone = "13800138001"
        # HB_bankcard = "5555666677778889"
        if environment == "SIT":
            hyzllg = Hyzllg(loanReqNo=HB_loanReqNo,
                            name=random__name,
                            idNo=generate__ID,
                            phone=HB_phone,
                            loanAmount=loanAmount,
                            periods=periods,
                            custGrde=custGrde,
                            bankcard=HB_bankcard,
                            url=res_url["sit_url_hb"],
                            res_data=res_data,
                            discountRate=discountRate)
        elif environment == "UAT":
            hyzllg = Hyzllg(loanReqNo=HB_loanReqNo,
                            name=random__name,
                            idNo=generate__ID,
                            phone=HB_phone,
                            loanAmount=loanAmount,
                            periods=periods,
                            custGrde=custGrde,
                            bankcard=HB_bankcard,
                            url=res_url["uat_url_hb"],
                            res_data=res_data,
                            discountRate=discountRate)
        elif environment == "DEV":
            hyzllg = Hyzllg(loanReqNo=HB_loanReqNo,
                            name=random__name,
                            idNo=generate__ID,
                            phone=HB_phone,
                            loanAmount=loanAmount,
                            periods=periods,
                            custGrde=custGrde,
                            bankcard=HB_bankcard,
                            url=res_url["dev_url_hb"],
                            res_data=res_data,
                            discountRate=discountRate)
        else:
            print("........")

        test_info = f'''
                        姓名：{random__name}
                        身份证号：{generate__ID}
                        手机号：{HB_phone}
                        借款金额:{loanAmount}
                        借款期次:{periods}
                        loanReqNo:{HB_loanReqNo}
                    '''
        insure_infos = hyzllg.insure_info()  # 投保信息接口
        Insure_Data_Query = hyzllg.insure_data_query(insure_infos)  # 投保资料查询接口
        hyzllg.insure(Insure_Data_Query)  # 投保接口
        hyzllg.disburse()  # 支用接口
        time.sleep(1)
        print(test_info)
        # raw_input("Press <enter>")

def main():
    #环境（sit,uat,dev）
    environment = "sit"
    #走数据笔数
    number = 1
    # 借款金额
    loanAmount = 6100
    # 期数
    periods = "6"
    # 客户等级
    custGrde = 18
    # 折后利率
    discountRate = 18
    hb_main(environment.upper(),number,loanAmount,periods,custGrde,discountRate)

if __name__ == '__main__':
    main()
