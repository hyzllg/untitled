import time
import yaml
from utils import lj_putout_mock, generate_customer_info,api_request


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
        self.res_data = kwargs["res_data"]
        self.custType = kwargs["custType"]


    def credit_granting(self):
        #获取res默认data并替换其中参数
        data = self.res_data["credit_granting"]
        data["channelCustId"]=self.channelCustId
        data["creditReqNo"]=self.creditReqNo
        data["name"]=self.name
        data["idNo"]=self.idNo
        data["phone"]=self.phone
        data["repayAmount"]=self.repayAmount
        data["periods"]=self.periods
        data["bankcard"]=self.bankcard
        data["custType"]=self.custType
        url = self.url["credit_granting"]
        print("**********授信申请**********")
        requit = api_request.request_api().test_api(url,data)
        try:
            if requit["result"] == True:
                creditApplyNo = requit["data"]["body"]["creditApplyNo"]
                print("授信接口调用成功！")
                if requit["data"]["body"]["status"] == "01":
                    print("授信受理成功，处理中！")
                else:
                    print("授信受理失败！")
                    exit()
            else:
                print("未知异常！")
                exit()
        except KeyError:
            print("甜橙授信接口响应异常！")
            exit()
        return creditApplyNo

    def credit_inquiry(self, creditApplyNo):
        hhh = 0
        data = self.res_data["credit_inquiry"]
        data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = self.creditReqNo
        data["creditApplyNo"] = creditApplyNo

        time.sleep(2)
        n = False
        while hhh < 16:
            url = self.url["credit_inquiry"]
            print("**********授信结果查询**********")
            requit = api_request.request_api().test_api(url,data)
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
            exit()
        return n

    def disburse_trial(self, capitalCode):
        data = self.res_data["disburse_trial"]
        data["channelCustId"] = self.channelCustId
        data["periods"] = self.periods
        data["loanAmount"] = self.loanAmount

        while True:
            url = self.url["disburse_trial"]
            print("**********支用试算**********")
            requit = api_request.request_api().test_api(url,data)
            try:
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
                    exit()
            except KeyError:
                print("甜橙支用试算接口响应异常！")
                exit()

    def disburse(self, capitalCode):
        data = self.res_data["disburse"]
        data["channelCustId"] = self.channelCustId
        data["loanReqNo"] = self.loanReqNo
        data["creditReqNo"] = self.creditReqNo
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankcard"] = self.bankcard
        data["phone"] = self.phone
        data["capitalCode"] = capitalCode
        data["custType"] = self.custType

        url = self.url["disburse"]
        print("**********支用接口**********")
        requit = api_request.request_api().test_api(url,data)
        try:
            if requit["result"] == True:
                print("支用接口调用成功！")
                if requit["data"]["body"]["status"] == "01":
                    print("受理成功，处理中!")
                else:
                    print("受理失败")
                    exit()
            else:
                print("未知异常！")
                exit()
        except KeyError:
            print("甜橙支用接口响应异常！")
            exit()

    def disburse_in_query(self, loanReqNo):
        data = self.res_data["disburse_in_query"]
        data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = loanReqNo
        data["loanReqNo"] = self.creditReqNo
        time.sleep(5)
        while True:
            url = self.url["disburse_in_query"]
            print("**********支用结果查询**********")
            requit = api_request.request_api().test_api(url,data)
            try:
                if requit["result"] == True:
                    print("支用结果查询接口调用成功！")
                    if requit["data"]["body"]["status"] == "01":
                        print("支用成功")
                        break
                    elif requit["data"]["body"]["status"] == "00":
                        print("处理中！")
                    else:
                        print("支用失败！")
                        exit()
                else:
                    print("未知异常！")
                    exit()
                time.sleep(3)
            except KeyError:
                print("甜橙支用结果查询接口响应异常！")
                exit()



def tc_main(number,repayAmount,loanAmount,periods,custType,capitalCode,environment,loan_datetime=time.strftime("%Y-%m-%d")):
    #获取配置信息
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    res_url = get_yaml_data('./conf/Config.yaml')["api_url_tc"]
    res_data = get_yaml_data('./conf/request_data.yaml')["tc_res_data"]
    abc=[]
    for i in range(number):
        # 指定姓名身份证手机号时使用
        # random_name = "张八"
        # generate__ID = "542128196305226980"
        # ORANGE_phone = "13800138001"
        # ORANGE_bankcard = "5555666677778889"
        idNo = generate_customer_info.customer().idNo()
        name = generate_customer_info.customer().name()
        phone = generate_customer_info.customer().phone()
        bankcard = generate_customer_info.customer().bankcard()

        channelCustId = generate_customer_info.customer().reqno(66)
        creditReqNo = generate_customer_info.customer().reqno(88)
        loanReqNo = generate_customer_info.customer().reqno(99)
        if environment == "SIT":
            hyzllg = Hyzllg(channelCustId=channelCustId,
                            creditReqNo=creditReqNo,
                            loanReqNo = loanReqNo,
                            name = name,
                            idNo = idNo,
                            phone = phone,
                            repayAmount = repayAmount,
                            loanAmount = loanAmount,
                            periods = periods,
                            bankcard = bankcard,
                            url = res_url["sit_url_tc"],
                            res_data = res_data,
                            custType = custType)
            credit = hyzllg.credit_granting()
            abc.append(
                {"channelCustId" : channelCustId,
                 "creditReqNo" : creditReqNo,
                 "loanReqNo" : loanReqNo,
                 "name" : name,
                 "idNo" : idNo,
                 "phone" : phone,
                 "repayAmount" : repayAmount,
                 "loanAmount" : loanAmount,
                 "periods" : periods,
                 "bankcard" : bankcard,
                 "url" : res_url["sit_url_tc"],
                 "res_data" : res_data,
                 "credit" : credit,
                 "custType" : custType})
        elif environment == "UAT":
            hyzllg = Hyzllg(channelCustId=channelCustId,
                            creditReqNo=creditReqNo,
                            loanReqNo = loanReqNo,
                            name = name,
                            idNo = idNo,
                            phone = phone,
                            repayAmount = repayAmount,
                            loanAmount = loanAmount,
                            periods = periods,
                            bankcard = bankcard,
                            url = res_url["uat_url_tc"],
                            res_data=res_data,
                            custType = custType)
            credit = hyzllg.credit_granting()
            abc.append(
                {"channelCustId" : channelCustId,
                 "creditReqNo" : creditReqNo,
                 "loanReqNo" : loanReqNo,
                 "name" : name,
                 "idNo" : idNo,
                 "phone" : phone,
                 "repayAmount" : repayAmount,
                 "loanAmount" : loanAmount,
                 "periods" : periods,
                 "bankcard" : bankcard,
                 "url" : res_url["uat_url_tc"],
                 "res_data": res_data,
                 "credit" : credit,
                 "custType" : custType})
        elif environment == "DEV":
            hyzllg = Hyzllg(channelCustId=channelCustId,
                            creditReqNo=creditReqNo,
                            loanReqNo = loanReqNo,
                            name = name,
                            idNo = idNo,
                            phone = phone,
                            repayAmount = repayAmount,
                            loanAmount = loanAmount,
                            periods = periods,
                            bankcard = bankcard,
                            url = res_url["dev_url_tc"],
                            res_data=res_data,
                            custType = custType)
            credit = hyzllg.credit_granting()
            abc.append(
                {"channelCustId" : channelCustId,
                 "creditReqNo" : creditReqNo,
                 "loanReqNo" : loanReqNo,
                 "name" : name,
                 "idNo" : idNo,
                 "phone" : phone,
                 "repayAmount" : repayAmount,
                 "loanAmount" : loanAmount,
                 "periods" : periods,
                 "bankcard" : bankcard,
                 "url" : res_url["dev_url_tc"],
                 "res_data": res_data,
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
                ljreqno = generate_customer_info.customer().reqno(55)
                lj_putout_mock.lj_mock().update_lj_mock("apply", ljreqno, loan_datetime ,environment)
                lj_putout_mock.lj_mock().update_lj_mock("query", ljreqno, loan_datetime ,environment)
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
                            res_data = i["res_data"],
                            custType = i['custType'])
            if hyzllg.credit_inquiry(i['credit']):
                hyzllg.disburse_trial(capitalCode)
                hyzllg.disburse(capitalCode)
                # Python_crawler.disburse_in_query(ORANGE_serial_number[2])
                abc.remove(i)
                nnn = True
            n += 1
            if n > 16 and nnn == False:
                exit()
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





