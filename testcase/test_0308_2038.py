import pytest
import random
import WZ_360
import requests
import json
import time
import re as res
import os
from past.builtins import raw_input
import Collect

class testadd:
    def monthperiod(self,periods,custGrde):
        random__name = Collect.random_name()
        generate__ID = Collect.generate_ID()
        HB_loanReqNo = Collect.loanReqNo()
        HB_phone = Collect.phone()
        Bank = Collect.bankcard()
        hyzllg = WZ_360.Hyzllg(HB_loanReqNo, random__name, generate__ID, HB_phone, "5000.00", periods, custGrde, Bank,
                            Collect.uat_url_360)
        insure = hyzllg.insure_info()
        hyzllg.insure_data_query(insure[-1])
        hyzllg.insure()
        hyzllg.disburse()
        #计算月保费期初本金比例
        a = str(round((custGrde/100 - 0.062 - custGrde/100*0.3)/24*(periods+1)/periods*100,2))
        print(a)
        #核心库里存的月保费期初本金比例
        discountRate = list(Collect.sql_cha(Collect.hxSIT_ORACLE,
                                              "select monthperiod from INSURE_SERIAL where idno = '{}'".format(
                                                  generate__ID))[0])[0]
        print(discountRate)
        return discountRate,a


class Testhyz:
    # def setup(self):
    #     print("每个方法执行前执行一次！")
    # def teardown(self):
    #     print("每个方法执行后执行一次！")
    #
    # def setup_class(self):
    #     print("每个类方法执行前执行一次！")
    # def teardown_class(self):
    #     print("每个类方法执行后执行一次！")
    def test001(self):
        print("这是第一条用例！")
        a = testadd().monthperiod(3, 27.31)
        #计算出的月保费期初本金比例
        b = a[1]
        #库里存的月保费期初本金比例
        c = a[0]
        assert b == c
    def test002(self):
        print("这是第二条用例！")
        a = testadd().monthperiod(6, 18.00)
        #计算出的月保费期初本金比例
        b = a[1]
        #库里存的月保费期初本金比例
        c = a[0]
        print(c)
        assert b == c

    def test003(self):
        print("这是第三条用例！")
        a = testadd().monthperiod(12, 25.99)
        #计算出的月保费期初本金比例
        b = a[1]
        #库里存的月保费期初本金比例
        c = a[0]
        assert b == c

if __name__ == '__main__':
    pytest.main()