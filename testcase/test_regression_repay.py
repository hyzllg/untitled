import os

import pytest

import Collect


class Test_repay_regression:
    Pay_time = "2028/08/24"
    data = ["787-502808233301498210", "787-502807273301494658", "787-502808233301498514", "787-502808233301498211"]

    @pytest.fixture(scope='function', params=data)
    def myfixture(self, request):
        return request.param
    def test001(self,myfixture):
        #借据表 贷款状态校验

        discountRate = list(Collect.sql_cha(Collect.zwSIT_ORACLE,
                                            "select loanstatus from acct_loan where serialno = '{}'".format(
                                                myfixture))[0])[0]
        assert discountRate == "20","校验贷款状态是否为20，当前的贷款状态为{}".format(discountRate)
    def test002(self,myfixture):
        #借据表 结清日期校验
        discountRate = list(Collect.sql_cha(Collect.zwSIT_ORACLE,
                                            "select finishdate from acct_loan where serialno = '{}'".format(
                                                myfixture))[0])[0]
        assert discountRate == self.Pay_time , "校验结清日期是否正确，当前的结清日期为%s"%discountRate
    def test003(self,myfixture):
        #还款计划表 校验应还和实还是否一致
        ACCT_PAYMENT_SCHEDULE = list(Collect.sql_cha(Collect.zwSIT_ORACLE,
                                            "select paycorpusamt，actualpaycorpusamt,payinteamt,actualpayinteamt,payfineamt,actualfineamt,paycompdinteamt,actualcompdinteamt,payfeeamt1,actualpayfeeamt1 from ACCT_PAYMENT_SCHEDULE where objectno = '{}'".format(
                                                myfixture)))
        for i in ACCT_PAYMENT_SCHEDULE:
            i = list(i)
            assert i[0] == i[1],"校验本金应还和实还是否一致，应还本金%s，实还本金%s"%(i[0],i[1])
            assert i[2] == i[3],"校验利息应还和实还是否一致，应还利息%s，实还利息%s"%(i[0],i[1])
            assert i[4] == i[5],"校验罚息应还和实还是否一致，应还罚息%s，实还罚息%s"%(i[0],i[1])
            assert i[6] == i[7],"校验复利应还和实还是否一致，应还复利%s，实还复利%s"%(i[0],i[1])
            assert i[8] == i[9],"校验保费应还和实还是否一致，应还保费%s，实还保费%s"%(i[0],i[1])





if __name__ == '__main__':
    pytest.main(['test_regression_0312.py::Test_repay_regression'])
    os.system('allure generate ./temp -o ./report --clean')