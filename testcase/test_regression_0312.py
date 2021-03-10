import pytest
import Automated_testing.Repay as repay
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
        assert discountRate == "20"
    def test002(self,myfixture):
        #借据表 结清日期校验
        discountRate = list(Collect.sql_cha(Collect.zwSIT_ORACLE,
                                            "select finishdate from acct_loan where serialno = '{}'".format(
                                                myfixture))[0])[0]
        assert discountRate == self.Pay_time
    def test003(self,myfixture):
        #还款计划表 校验应还和实还是否一致
        ACCT_PAYMENT_SCHEDULE = list(Collect.sql_cha(Collect.zwSIT_ORACLE,
                                            "select paycorpusamt，actualpaycorpusamt,payinteamt,actualpayinteamt,payfineamt,actualfineamt,paycompdinteamt,actualcompdinteamt,payfeeamt1,actualpayfeeamt1 from ACCT_PAYMENT_SCHEDULE where objectno = '{}'".format(
                                                myfixture)))
        for i in ACCT_PAYMENT_SCHEDULE:
            i = list(i)
            assert i[0] == i[1]
            assert i[2] == i[3]
            assert i[4] == i[5]
            assert i[6] == i[7]
            assert i[8] == i[9]





if __name__ == '__main__':
    pytest.main(['test_regression_0312.py::Test_repay_regression'])