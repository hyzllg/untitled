# -*- coding: utf-8 -*-

import unittest

import requests

from mathfunc import *


class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("do something before test.Prepare environment.")
        #准备环境，用例开始执行前执行一次

    @classmethod
    def tearDownClass(cls):
        print("do something after test.Clean up.")
        # 清理环境，用例执行完后执行一次

    def test_phone01(self):
        self.assertEqual("Return Successd!",phone_01()["reason"])
        self.assertEqual("200",phone_01()["resultcode"])

    def test_phone02(self):
        self.assertEqual("错误的请求KEY!!",phone_02()["reason"])


if __name__ == '__main__':
    unittest.main()