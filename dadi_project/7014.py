import time
import yaml
from utils import lj_putout_mock, generate_customer_info,api_request,database_manipulation,my_log


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
        self.log = my_log.Log()


    def credit_granting(self):
        #获取res默认data并替换其中参数
        data = self.res_data["credit_granting"]
        data["channelCustId"]=self.channelCustId
        data["creditReqNo"]=self.creditReqNo
        data["name"]=self.name
        data["idNo"]=self.idNo
        data["phone"]=self.phone
        data["loanAmount"]=self.repayAmount
        data["periods"]=self.periods
        data["bankCard"]=self.bankcard
        data['bankPhone']=self.phone
        data["custType"]=self.custType
        url = self.url["credit_granting"]

        self.log.info("授信申请")
        self.log.info(f"[{url}]")

        requit = api_request.request_api().test_api("post", url, data)
        try:
            if requit["result"] == True:
                creditApplyNo = requit["data"]["body"]["creditApplyNo"]
                self.log.info("授信接口调用成功！")
                if requit["data"]["body"]["status"] == "01":
                    self.log.info("授信受理成功，处理中！")
                else:
                    self.log.error("授信受理失败！")
                    exit()
            else:
                self.log.error("未知异常！")
                exit()
        except KeyError:
            self.log.error("甜橙授信接口响应异常！")
            exit()
        return creditApplyNo

    def credit_inquiry(self, creditApplyNo):
        hhh = 0
        data = self.res_data["credit_inquiry"]
        data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = self.creditReqNo
        data["creditApplyNo"] = creditApplyNo
        n = False
        while hhh < 16:
            url = self.url["credit_inquiry"]
            self.log.info("授信结果查询")
            self.log.info([url])
            requit = api_request.request_api().test_api("post", url, data)
            self.log.info("授信查询接口调用成功！")
            try:
                if requit["data"]["body"]["status"] == "01":
                    self.log.info("授信通过！")
                    n = True
                    break
                elif requit["data"]["body"]["status"] == "00":
                    self.log.info("授信中！")
                    time.sleep(3)
                    hhh += 1
                    continue
                else:
                    self.log.error("授信失败！")
                    exit()
            except KeyError:
                self.log.error("甜橙授信查询接口响应异常！")
                exit()
        if hhh >= 16:
            self.log.error("甜橙授信时间过长！可能由于授信挡板问题，结束程序！")
            exit()
        return n

    def disburse_trial(self, capitalCode):
        data = self.res_data["disburse_trial"]
        data["channelCustId"] = self.channelCustId
        data["periods"] = self.periods
        data["loanAmount"] = self.loanAmount

        while True:
            url = self.url["disburse_trial"]
            self.log.info("支用试算")
            self.log.info(url)
            requit = api_request.request_api().test_api("post", url, data)
            try:
                if requit["result"] == True:
                    self.log.info(f'本次试算资方为：{requit["data"]["body"]["capitalCode"]}')
                    if requit["data"]["body"]["status"] == "01" and requit["data"]["body"]["capitalCode"] == capitalCode:
                        self.log.info("支用试算成功！")
                        break
                    else:
                        time.sleep(3)
                        continue
                else:
                    self.log.error("未知异常！")
                    exit()
            except KeyError:
                self.log.error("甜橙支用试算接口响应异常！")
                exit()

    def disburse(self, capitalCode):
        data = self.res_data["disburse"]
        data["channelCustId"] = self.channelCustId
        data["loanReqNo"] = self.loanReqNo
        data["creditReqNo"] = self.creditReqNo
        data["loanAmount"] = self.loanAmount
        data["periods"] = self.periods
        data["bankCard"] = self.bankcard
        data["bankPhone"] = self.phone
        data["capitalCode"] = capitalCode
        data["custType"] = self.custType

        url = self.url["disburse"]
        self.log.info("支用接口")
        self.log.info(url)
        requit = api_request.request_api().test_api("post", url, data)
        try:
            if requit["result"] == True:
                self.log.info("支用接口调用成功！")
                if requit["data"]["body"]["status"] == "01":
                    self.log.info("受理成功，处理中!")
                else:
                    self.log.info("受理失败")

                    exit()
            else:
                self.log.info("未知异常！")

                exit()
        except KeyError:
            self.log.info("甜橙支用接口响应异常！")

            exit()

    def disburse_in_query(self, loanReqNo):
        data = self.res_data["disburse_in_query"]
        data["channelCustId"] = self.channelCustId
        data["creditReqNo"] = loanReqNo
        data["loanReqNo"] = self.creditReqNo
        time.sleep(5)
        while True:
            url = self.url["disburse_in_query"]
            self.log.info("支用结果查询")
            self.log.info(url)

            requit = api_request.request_api().test_api("post", url, data)
            try:
                if requit["result"] == True:
                    self.log.info("支用结果查询接口调用成功！")
                    if requit["data"]["body"]["status"] == "01":
                        self.log.info("支用成功")

                        break
                    elif requit["data"]["body"]["status"] == "00":
                        self.log.info("处理中！")

                    else:
                        self.log.info("支用失败！")

                        exit()
                else:
                    self.log.info("未知异常！")

                    exit()
                time.sleep(3)
            except KeyError:
                self.log.info("甜橙支用结果查询接口响应异常！")

                exit()

def get_oracle_conf(conf,environment):
    if environment == "SIT":
        oracle_conf = conf['xshx_oracle']['xsxb_sit_oracle']
    elif environment == "UAT":
        oracle_conf = conf['xshx_oracle']['xsxb_uat_oracle']
    elif environment == "DEV":
        oracle_conf = conf['xshx_oracle']['xsxb_dev_oracle']
    return oracle_conf


def tc_main(number,repayAmount,loanAmount,periods,custType,capitalCode,environment,loan_datetime=time.strftime("%Y-%m-%d")):
    #获取配置信息
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    conf = get_yaml_data('./conf/Config.yaml')
    res_url = conf["api_url_tc"]
    res_data = get_yaml_data('./conf/request_data.yaml')["tc_res_data"]
    #日志
    log = my_log.Log()
    #获取数据库配置
    oracle_conf = get_oracle_conf(conf,environment)
    hx_oracle = database_manipulation.Oracle_Class(oracle_conf[0], oracle_conf[1], oracle_conf[2])
    abc=[]
    for i in range(number):
        # 指定姓名身份证手机号时使用
        # name = "张三"
        # idNo = "653221198609178486"
        # phone = "15838434412"
        # bankcard = "6216261000000000018"
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
                log.info("更新客户信息表liveaddress")
                sql = "update customer_info set liveaddress = '北京市市辖区东城区' where CERTID = '%s'" % i['idNo']
                log.info(sql)
                hx_oracle.insert_update_data(sql)

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
            log.info(test_info)
    hx_oracle.close_all()


def main():
    #环境（sit,uat,dev）
    environment = "sit"
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





