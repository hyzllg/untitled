import time
import re as res
import yaml
from utils import generate_customer_info,api_request,database_manipulation,Log


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
        self.log = Log.Log()


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
        requit = api_request.request_api().test_api(url,data)
        try:
            if requit["result"] == True:
                self.log.info("投保信息接口成功！")
                a = requit["data"]["insurAgencyUrl"]
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
        requit = api_request.request_api().test_api(url,data)
        try:
            if requit["result"] == True:
                self.log.info("投保资料查询成功！")
            else:
                self.log.error("投保资料查询失败！")
                exit()
        except KeyError:
            self.log.error("还呗投保资料查询接口响应异常！")
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
        self.log.info("投保接口")
        self.log.info(url)
        requit = api_request.request_api().test_api(url,data)
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
            self.log.error("还呗投保接口响应异常！")
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
        self.log.info("支用接口")
        self.log.info(url)
        requit = api_request.request_api().test_api(url,data)
        try:
            if requit["result"] == True:
                try:

                    if requit["data"]["status"] == "01":
                        self.log.info("支用受理成功，处理中！")
                    elif requit["data"]["status"] == "00":
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
    conf = get_yaml_data('./conf/Config.yaml')
    res_url = conf["api_url_hb"]
    res_data = get_yaml_data('./conf/request_data.yaml')["hb_res_data"]
    #获取数据库配置
    oracle_conf = get_oracle_conf(conf,environment)
    hx_oracle = database_manipulation.Oracle_Class(oracle_conf[0], oracle_conf[1], oracle_conf[2])

    for i in range(number):
        HB_loanReqNo = generate_customer_info.customer().reqno(66)
        idNo = generate_customer_info.customer().idNo()
        name = generate_customer_info.customer().name()
        HB_phone = generate_customer_info.customer().phone()
        HB_bankcard = generate_customer_info.customer().bankcard()
        # 指定姓名身份证手机号时使用
        # random__name = "张八"
        # generate__ID = "542128196305226980"
        # HB_phone = "13800138001"
        # HB_bankcard = "5555666677778889"
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
        time.sleep(5)
        log = Log.Log()
        log.info("更新customer_info表liveaddress")
        sql = "update customer_info set liveaddress = '河北省石家庄市裕华区体育南大街379号11栋3单元403号' where CERTID = '%s'" % idNo
        log.info(sql)
        hx_oracle.insert_update_data(sql)
        log.info(test_info)
    hx_oracle.close_all()

def main():
    #环境（sit,uat,dev）
    environment = "sit"
    #走数据笔数
    number =1
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
