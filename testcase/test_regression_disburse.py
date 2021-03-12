import os
import time

import pytest
import Collect
import WZ_PPDAI
import WZ_360
import WZ_HUANBEI
import WZ_ORANGE

def disburse_360():
    random__name = Collect.random_name()
    HB_loanReqNo = Collect.loanReqNo()
    HB_phone = Collect.phone()
    Bank = Collect.bankcard()
    generate__ID = Collect.id_card().generate_ID()
    #借款金额
    loanAmount = 5000
    #期数
    periods = '3'
    #客户等级
    custGrde = 26.00
    hyzllg = WZ_360.Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, Bank,
                    Collect.sit_url_360)
    insure = hyzllg.insure_info()
    hyzllg.insure_data_query(insure[-1])
    hyzllg.insure()
    hyzllg.disburse()
    return HB_loanReqNo

def disburse_ppd():
    random__name = Collect.random_name()
    HB_loanReqNo = Collect.loanReqNo()
    HB_creditReqNo = Collect.creditReqNo()
    HB_phone = Collect.phone()
    generate__ID = Collect.id_card().generate_ID()
    HB_bankcard = Collect.bankcard()
    # 借款金额
    loanAmount = 5000
    # 期数
    periods = "6"
    # 客户等级上下限
    # custGrde = list(Collect.sql_cha(Collect.hxSIT_ORACLE,"select t.attribute1 from code_library t where t.codeno ='PaiPaiDai'and t.itemno = '{}'".format(periods))[0])[0]
    custGrde = 26.32

    hyzllg = WZ_PPDAI.Hyzllg(HB_loanReqNo, HB_creditReqNo, random__name, generate__ID, HB_phone, loanAmount, periods,
                    HB_bankcard,
                    "建设银行", HB_phone, Collect.sit_url_pp, custGrde)
    insure = hyzllg.insure_info()  # 投保信息接口
    Insure_Data_Query = hyzllg.insure_data_query(insure[-1])  # 投保资料查询接口
    hyzllg.insure(Insure_Data_Query[3])  # 投保接口
    hyzllg.credit_granting()  # 授信接口
    if hyzllg.credit_inquiry()[-1]:
        hyzllg.disburse()
    return HB_creditReqNo

def disburse_hb():
    random__name = Collect.random_name()
    generate__ID = Collect.id_card().generate_ID()
    HB_loanReqNo = Collect.loanReqNo()
    HB_phone = Collect.phone()
    HB_bankcard = Collect.bankcard()
    #借款金额
    loanAmount = 5000
    #期数
    periods = "6"
    #客户等级
    custGrde = 26.00
    #折后利率
    discountRate = list(Collect.sql_cha(Collect.hxSIT_ORACLE,"select attribute1 t from code_library t where t.codeno ='HuanbeiArte' and t.itemno = '{}'".format(periods))[0])[0]
    hyzllg = WZ_HUANBEI.Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, loanAmount, periods, custGrde, HB_bankcard,
                Collect.sit_url_hb, discountRate)
    hyzllg.insure_info()   #投保信息接口
    Insure_Data_Query = hyzllg.insure_data_query()   #投保资料查询接口
    hyzllg.insure(Insure_Data_Query[3])  #投保接口
    hyzllg.disburse()   #支用接口
    return HB_loanReqNo

def disburse_tc():
    random__name = Collect.random_name()
    generate__ID = Collect.id_card().generate_ID()
    ORANGE_phone = Collect.phone()
    ORANGE_bankcard = Collect.bankcard()
    channelCustId = Collect.channelCustId()
    creditReqNo = Collect.creditReqNo()
    loanReqNo = Collect.loanReqNo()
    # 借款金额
    loanAmount = 5000
    # 期数
    periods = "6"
    hyzllg = WZ_ORANGE.Hyzllg(channelCustId, creditReqNo, loanReqNo, random__name, generate__ID, ORANGE_phone,
                    loanAmount, periods, ORANGE_bankcard, Collect.sit_url_tc)
    credit = hyzllg.credit_granting()[-1]
    if hyzllg.credit_inquiry(credit[-1])[-1]:
        hyzllg.disburse_trial('FBBANK')
        hyzllg.disburse('FBBANK')
    return creditReqNo

def list_idcard():
    list_idcard_data = []
    # list_idcard_data.append(disburse_ppd())
    list_idcard_data.append(disburse_360())
    # list_idcard_data.append(disburse_hb())
    # list_idcard_data.append(disburse_tc())
    return list_idcard_data
if __name__ == '__main__':
    # data = list_idcard()
    # time.sleep(60)
    data = ["20210312103536689394","20210312103535683652"]
    while data:
        for i in data:
            status = Collect.sql_cha(Collect.hxSIT_ORACLE,"select showstate from putout_approve where creditreqno = '{}'".format(i))[0][0]
            print(f"放款状态：{status}")
            if status == "1":
                data.remove(i)
                with open(r'test.txt','a') as f:
                    f.write(f"{i}\n")
            elif status == "5":
                print("放款失败！")
                break
            else:
                time.sleep(10)
                continue




