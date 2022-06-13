import os
import time
import re as res
import yaml
from utils import generate_customer_info,api_request,my_log


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
        self.log = my_log.Log()


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
        self.log.info("投保信息接口")
        self.log.info(url)
        result = api_request.request_api().test_api("post", url, data)
        try:
            if result["result"] == True:
                self.log.info("投保信息接口成功！")
                a = result["data"]["insurAgencyUrl"]
                b = res.search("lp=(.*)", a)
                c = b.group()[3:]
            else:
                self.log.error("投保信息接口失败！")
                exit()
        except KeyError:
            self.log.error("还呗投保信息接口响应异常！")
            exit()
        return c

    def insure_data_query(self, token):
        data = self.res_data["insure_data_query"]
        data["loanReqNo"] = self.loanReqNo
        data["token"] = token
        url = self.url['insure_data_query']
        self.log.info("投保资料查询接口")
        self.log.info(url)
        result = api_request.request_api().test_api("post",url, data)
        try:
            if result["result"] == True:
                self.log.info("投保资料查询成功！")
            else:
                self.log.error("投保资料查询失败！")
                exit()
        except KeyError:
            self.log.error("还呗投保资料查询接口响应异常！")
            exit()
        return result["data"]["premiumRate"]

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
        self.log.info("投保接口")
        self.log.info(url)
        result = api_request.request_api().test_api("post", url, data)
        try:
            if result["result"] == True:
                try:
                    if result["data"]["message"]:
                        self.log.error("受理失败")
                        exit()
                except BaseException as e:
                    if result["data"]["status"] == '01':
                        self.log.info("已受理，处理中！")
            else:
                self.log.error("未知异常！")
                exit()
        except KeyError:
            self.log.error("还呗投保接口响应异常！")
            exit()
        return result

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
        self.log.info("支用接口")
        self.log.info(url)
        result = api_request.request_api().test_api("post", url, data)
        try:
            if result["result"] == True:
                try:

                    if result["data"]["status"] == "01":
                        self.log.info("支用受理成功，处理中！")
                    elif result["data"]["status"] == "00":
                        self.log.error("受理失败！")
                        exit()
                except BaseException as e:
                    self.log.error("未知异常！")
                    exit()
            else:
                self.log.error("未知异常！")
                exit()
        except KeyError:
            self.log.error("还呗支用接口响应异常！")
            exit()
def get_oracle_conf(conf,environment):
    oracle_conf = ''
    if environment == "SIT":
        oracle_conf = conf['xshx_oracle']['xsxb_sit_oracle']
    elif environment == "UAT":
        oracle_conf = conf['xshx_oracle']['xsxb_uat_oracle']
    elif environment == "DEV":
        oracle_conf = conf['xshx_oracle']['xsxb_dev_oracle']
    return oracle_conf

def hb_main(environment,number,loanAmount,periods,custGrde,discountRate):
    #获取配置信息
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    path = os.path.dirname(os.path.dirname(__file__))
    res_url = get_yaml_data(f'{path}/conf/url_res/api_url_hb.yaml')
    res_data = get_yaml_data(f'{path}/conf/loan_res/hb_res_data.yaml')

    for i in range(number):
        HB_loanReqNo = generate_customer_info.customer().reqno(66)
        idNo = generate_customer_info.customer().idNo()
        name = generate_customer_info.customer().name()
        HB_phone = generate_customer_info.customer().phone()
        HB_bankcard = generate_customer_info.customer().bankcard()
        # 指定姓名身份证手机号时使用
        # name = "龚笑彩"
        # idNo = "110109199609055730"
        # HB_phone = "16608134504"
        # HB_bankcard = "6230580000170395656"
        if environment == "SIT":
            hyzllg = Hyzllg(loanReqNo=HB_loanReqNo,
                            name=name,
                            idNo=idNo,
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
                            name=name,
                            idNo=idNo,
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
                            name=name,
                            idNo=idNo,
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
                        姓名：{name}
                        身份证号：{idNo}
                        手机号：{HB_phone}
                        借款金额:{loanAmount}
                        借款期次:{periods}
                        loanReqNo:{HB_loanReqNo}
                    '''
        insure_infos = hyzllg.insure_info()  # 投保信息接口
        Insure_Data_Query = hyzllg.insure_data_query(insure_infos)  # 投保资料查询接口
        hyzllg.insure(Insure_Data_Query)  # 投保接口
        hyzllg.disburse()  # 支用接口
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
    # 客户等级
    custGrde = 18
    # 折后利率
    discountRate = 18
    hb_main(environment.upper(),number,loanAmount,periods,custGrde,discountRate)

if __name__ == '__main__':
    main()
