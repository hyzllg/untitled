import unittest
import HTMLTestRunner
import requests


class TestMathMethod(unittest.TestCase):
    def test_testcase01(self):
        url = 'http://apis.juhe.cn/mobile/get'
        params = {
            "key":"587a63506ac7c9ea98f3946631f3abfb",
            "phone":"16621381003"
        }
        res = requests.get(url,params=params)
        result = res.json()
        print(result)
        self.assertEqual("Return Successd!", result["reason"], msg="预期结果与实际结果不相等")


# 作用：在别的地方引用此模块，调试的代码不会被导入
if __name__ == "__main__":  # 程序入口
    unittest.main()  # 执行当前页面test_开头的所有用例
