import os

import pytest
import WZ_PPDAI
import Collect
# print(Collect.PMT(27.31,12,6.2))


def disburse_ppd(custGrde,periods):
    random__name = Collect.random_name()
    HB_loanReqNo = Collect.loanReqNo()
    HB_creditReqNo = Collect.creditReqNo()
    HB_phone = Collect.phone()
    generate__ID = Collect.id_card().generate_ID()
    HB_bankcard = Collect.bankcard()
    # 借款金额
    loanAmount = 5000
    # 期数
    # periods = "6"
    # 客户等级上下限
    # custGrde = list(Collect.sql_cha(Collect.hxSIT_ORACLE,"select t.attribute1 from code_library t where t.codeno ='PaiPaiDai'and t.itemno = '{}'".format(periods))[0])[0]
    # custGrde = 26.32

    hyzllg = WZ_PPDAI.Hyzllg(HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,
                    HB_bankcard,
                    "建设银行", HB_phone, Collect.sit_url_pp, custGrde)
    insure = hyzllg.insure_info()  # 投保信息接口
    Insure_Data_Query = hyzllg.insure_data_query(insure[-1])  # 投保资料查询接口
    hyzllg.insure(Insure_Data_Query[3])  # 投保接口
    hyzllg.credit_granting()  # 授信接口
    # if hyzllg.credit_inquiry()[-1]:
    #     hyzllg.disburse()
    data = Collect.sql_cha(Collect.hxSIT_ORACLE,"select MONTHPERIOD from INSURE_SERIAL where idno = '{}'".format(generate__ID))[0][0]
    return data

class Test_MONTHPERIOD():
    test_data = [[18.00,3,6.2],[22.22,3,6.2],[23.45,6,6.2],[27.31,6,6.2],[24.55,12,6.2],[23.86,12,6.2]]
    @pytest.mark.parametrize("a",test_data)
    def test001(self,a):
        assert disburse_ppd(a[0],a[1]) == str(Collect.PMT(a[0],a[1],a[2])),"验证月保费起初本金比例"


pytest.main(["test.py::Test_MONTHPERIOD::test001"])
os.system("allure generate ./temp -o ./report --clean")