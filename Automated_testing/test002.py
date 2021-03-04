import unittest
# 中文 Chinese
from HwTestReport import HTMLTestReport

# 英文 English
from HwTestReport import HTMLTestReportEN

class Case_assert_1(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_ok(self):
        self.assertEqual(1,1)

    def test_faile(self):
        self.assertEqual(1,2)

    def test_error(self):
        raise Exception

class Case_assert_2(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_ok(self):
        self.assertTrue(True)

class Case_assert_3(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_error(self):
        raise Exception

class Case_assert_4(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_faile(self):
        self.assertEqual(1,3)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Case_assert_1('test_ok'))
    suite.addTest(Case_assert_1('test_faile'))
    suite.addTest(Case_assert_1('test_error'))
    suite.addTest(Case_assert_2('test_ok'))
    suite.addTest(Case_assert_3('test_error'))
    suite.addTest(Case_assert_4('test_faile'))

    # English：HTMLTestReportEN
    with open('./HwTestReport.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='HwTestReport 测试',
                                description='带饼图，带详情',
                                tester='hyzllg')
        runner.run(suite)