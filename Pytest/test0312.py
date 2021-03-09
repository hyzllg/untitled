import WZ_PPDAI
from Collect import Collect


class Mytestcase():

    def test_001(self,periods,custGrde):
        sit_url = 'http://10.1.14.106:27405/channel/TEST/PPDAI/'
        uat_url = 'http://10.1.14.117:27405/channel/apitest/PPDAI/'
        dev_url = 'http://10.1.14.106:27405/channel-dev/apitest/PPDAI/'
        hxSIT_ORACLE = ["xbhxbusi", "ccic1234", "10.1.12.141:1521/PTST12UF"]
        random__name = Collect().random_name()
        HB_loanReqNo = Collect().loanReqNo()
        HB_creditReqNo = Collect().creditReqNo()
        HB_phone = Collect().phone()
        generate__ID = Collect().generate_ID()
        HB_bankcard = Collect().bankcard()
        #借款金额
        loanAmount = 5000
        #期数
        periods = periods
        #客户等级上下限
        custGrde = custGrde

        hyzllg = WZ_PPDAI.Hyzllg(HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,
                        HB_bankcard,
                        "建设银行", HB_phone, sit_url, custGrde)
        insure = hyzllg.insure_info()  # 投保信息接口
        Insure_Data_Query = hyzllg.insure_data_query(insure[-1])  # 投保资料查询接口
        hyzllg.insure(Insure_Data_Query[3])  # 投保接口
        hyzllg.credit_granting()  # 授信接口

        monthperiod = list(Collect().sql_cha(hxSIT_ORACLE,
                                              "select monthperiod from INSURE_SERIAL where idno = '{}'".format(
                                                  generate__ID))[0])[0]
        return monthperiod

# a = Mytestcase().test_001(3,26.66)
# print(a)