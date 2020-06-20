# -*- coding: utf-8 -*-

# import unittest
# from mathfunc import *
#
#
# class TestMathFunc(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         #Class前置条件
#         print("setUp Class")
#
#     @classmethod
#     def tearDownClass(cls):
#         #Class后置条件
#         print("tearDown Class")
#
#     def test_phone01(self):
#         self.assertEqual("Return Successd!",phone_01()["reason"])
#         self.assertEqual("200",phone_01()["resultcode"])
#
#     def test_phone02(self):
#         self.assertEqual("错误的请求KEY!!",phone_02()["reason"])
#
#
# if __name__ == '__main__':
#     unittest.main()
import time
import unittest

from selenium import webdriver

class TestMathCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def test_Case_01(self):
        url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
        self.driver.get(url)
        self.driver.find_element_by_name("accounts").send_keys('hyzllg')
        self.driver.find_element_by_name("pwd").send_keys('1234567890')
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button").click()



if __name__ == '__main__':
    unittest.main()











