import unittest
import WZ_PPDAI
from Collect import Collect
from HwTestReport import HTMLTestReport


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


class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_001(self):
        result = Mytestcase().test_001(3,26.66)
        self.assertEqual(result, '1.147')
    def test_002(self):
        result = Mytestcase().test_001(6,27.11)
        self.assertEqual(result, '1.04')
    def test_003(self):
        result = Mytestcase().test_001(9,18.11)
        self.assertEqual(result, '0.566')
    def test_004(self):
        result = Mytestcase().test_001(12,22.99)
        self.assertEqual(result, '0.791')


if __name__ == '__main__':
    #测试套件
    suite = unittest.TestSuite()
    suite.addTest(MyTest('test_001'))
    suite.addTest(MyTest('test_002'))
    suite.addTest(MyTest('test_003'))
    suite.addTest(MyTest('test_004'))

    with open('./HwTestReport.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='HwTestReport 测试',
                                description='带饼图，带详情',
                                tester='hyzllg')

        runner.run(suite)
