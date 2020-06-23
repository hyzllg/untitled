# -*- coding: utf-8 -*-

import unittest
from mathfunc import *


class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #Class前置条件
        print("setUp Class")

    @classmethod
    def tearDownClass(cls):
        #Class后置条件
        print("tearDown Class")

    def test_phone01(self):
        self.assertEqual("Return Successd!",phone_01()["reason"])
        self.assertEqual("200",phone_01()["resultcode"])

    def test_phone02(self):
        self.assertEqual("错误的请求KEY!!",phone_02()["reason"])


if __name__ == '__main__':
    unittest.main()










