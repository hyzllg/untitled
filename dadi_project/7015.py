import re as res
import time
import yaml
from utils import lj_putout_mock, generate_customer_info,api_request


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
        self.custGrde = kwargs["custGrde"]
        self.capitalCode = kwargs["capitalCode"]
        self.res_data = kwargs["res_data"]

    def insure_info(self):
        data = self.res_data["insure_info"]
        data["name"] = self.name
        data["insuranceNo"] = self.loanReqNo
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["periods"] = self.periods
        data["amount"] = self.loanAmount
        data["capitalCode"] = self.capitalCode
        data["custGrde"] = self.custGrde
        url = self.url["insure_info"]
        print("**********投保信息接口**********")
        requit = api_request.request_api().test_api(url,data)
        try:
            if requit["data"]["status"] == '01':
                a = requit["data"]["insurUrl"]
                b = res.search("lp=(.*)", a)
                c = b.group()[3:]
                print("投保信息接口成功！")
            else:
                print("投保信息接口失败！")
                exit()
        except KeyError:
            print("360投保信息接口响应异常！")
            exit()
        return c,data

    def insure_data_query(self, token):
        data = self.res_data["insure_data_query"]
        data["loanReqNo"] = self.loanReqNo
        data["token"] = token
        print("**********投保资料查询接口**********")
        url = self.url["insure_data_query"]
        requit = api_request.request_api().test_api(url,data)
        try:
            if requit["result"] == True:
                print("投保资料查询成功！")
            else:
                print("投保资料查询失败！")
                exit()
        except KeyError:
            print("360投保资料查询接口响应异常！")
            exit()

    def insure(self):
        data = self.res_data["insure"]
        data["loanReqNo"] = self.loanReqNo
        data["insReqNo"] = self.loanReqNo
        data["name"] = self.name
        data["idNo"] = self.idNo
        data["phone"] = self.phone
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        print("**********投保接口**********")
        url = self.url["insure"]
        requit = api_request.request_api().test_api(url,data)
        try:
            if requit["result"] == True:
                try:
                    if requit["data"]["message"]:
                        print("受理失败")
                        exit()
                except BaseException as e:
                    if requit["data"]["status"] == '01':
                        print("已受理，处理中！")
            else:
                print("未知错误！")
                exit()
        except KeyError:
            print("360投保接口响应异常！")
            exit()

    def disburse(self):
        data = self.res_data["disburse"]
        data["loanReqNo"] = self.loanReqNo
        data["idNo"] = self.idNo
        data["insuranceNo"] = self.loanReqNo
        data["phone"] = self.phone
        data["loanAmount"] = self.loanAmount
        data["name"] = self.name
        data["bankCard"] = self.bankcard
        data["periods"] = self.periods
        data["capitalCode"] = self.capitalCode
        data["custGrde"] = self.custGrde
        print("**********支用接口**********")
        url = self.url["disburse"]
        requit = api_request.request_api().test_api(url,data)
        try:
            if requit["result"] == True:
                if requit["data"]["status"] == "01":
                    print("放款受理成功，处理中！")
                elif requit["data"]["status"] == "00":
                    print("受理失败！")
                    exit()
            else:
                print("未知错误！")
                exit()
        except KeyError:
            print("360支用接口响应异常！")
            exit()

    def disburse_in_query(self, test_info):
        data = self.res_data['disburse_in_query']
        data["loanReqNo"] = self.loanReqNo
        while True:
            time.sleep(3)
            print("**********放款结果查询接口**********")
            url = self.url["disburse_in_query"]
            requit = api_request.request_api().test_api(url,data)
            try:
                if requit["result"] == True:
                    print("放款结果查询接口调用成功！")
                    if requit["data"]["status"] == '01':
                        print("支用成功，银行放款成功！")
                        print(test_info)
                    elif requit["data"]["status"] == '00':
                        print("支用中，银行放款中")
                        continue
                    elif requit["data"]["status"] == '03':
                        print("授信审批中")
                        continue
                    elif requit["data"]["status"] == '04':
                        print("授信审批成功")
                        continue
                    elif requit["data"]["status"] == '05':
                        print("授信审批拒绝")
                        exit()
                    elif requit["data"]["status"] == '02':
                        print("支用失败，银行放款失败")
                        exit()
                    else:
                        print("未知错误！")
                        exit()

                else:
                    print("未知错误！")
                    exit()
            except KeyError:
                print("360支用结果查询接口响应异常！")
                exit()


def main_360(environment,number,loanAmount,periods,custGrde,capitalCode):
    #获取配置信息
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    res_url = get_yaml_data('./conf/Config.yaml')["api_url_360"]
    res_data = get_yaml_data('./conf/request_data.yaml')["360_res_data"]
    for i in range(number):
        loanReqNo = generate_customer_info.customer().reqno(66)
        idNo = generate_customer_info.customer().idNo()
        name = generate_customer_info.customer().name()
        phone = generate_customer_info.customer().phone()
        Bank = generate_customer_info.customer().bankcard()
        #指定姓名身份证手机号时使用
        # name = "粱九广"
        # idNo = "330701199307093208"
        # HB_phone = "15776631124"
        # Bank = "6214661022113802"

        # （参数1：apply/query；参数2：流水号；参数3：放款时间，格式y-m-d)
        if capitalCode == "LJBANK":
            loan_datetime = time.strftime("%Y-%m-%d")
            ljreqno = generate_customer_info.customer().reqno(55)
            lj_putout_mock.lj_mock().update_lj_mock("apply", ljreqno, loan_datetime,environment)
            lj_putout_mock.lj_mock().update_lj_mock("query", ljreqno, loan_datetime,environment)
        if environment == "SIT":
            hyzllg = Hyzllg(loanReqNo = loanReqNo,
                            name = name,
                            idNo = idNo,
                            phone = phone,
                            loanAmount = loanAmount,
                            periods = periods,
                            custGrde = custGrde,
                            capitalCode = capitalCode,
                            bankcard = Bank,
                            url = res_url["sit_url_360"],
                            res_data = res_data
                            )
        elif environment == "UAT":
            hyzllg = Hyzllg(loanReqNo = loanReqNo,
                            name = name,
                            idNo = idNo,
                            phone = phone,
                            loanAmount = loanAmount,
                            periods = periods,
                            custGrde = custGrde,
                            capitalCode = capitalCode,
                            bankcard = Bank,
                            url = res_url["uat_url_360"],
                            res_data = res_data
                            )
        elif environment == "DEV":
            hyzllg = Hyzllg(loanReqNo = loanReqNo,
                            name = name,
                            idNo = idNo,
                            phone = phone,
                            loanAmount = loanAmount,
                            periods = periods,
                            custGrde = custGrde,
                            capitalCode = capitalCode,
                            bankcard = Bank,
                            url = res_url["dev_url_360"],
                            res_data = res_data
                            )
        else:
            print("........")

        test_info = f'''
                        姓名：{name}
                        身份证号：{idNo}
                        手机号：{phone}
                        借款金额:{loanAmount}
                        借款期次:{periods}
                        loanReqNo:{loanReqNo}
                    '''
        insure = hyzllg.insure_info()[0]
        hyzllg.insure_data_query(insure)
        hyzllg.insure()
        hyzllg.disburse()
        # Python_crawler.disburse_in_query(test_info)
        time.sleep(1)
        print(test_info)
        # raw_input("Press <enter>")



def main():
    #环境（sit,uat,dev）
    environment = "uat"
    #走数据笔数
    number = 1
    # 借款金额
    loanAmount = 6000
    # 期数
    periods = '6'
    # 客户等级
    custGrde = 18
    # 资方代码 (微众：FBBANK，龙江：LJBANK)
    capitalCode = "FBBANK"
    main_360(environment.upper(),number,loanAmount,periods,custGrde,capitalCode)

if __name__ == '__main__':
    main()
