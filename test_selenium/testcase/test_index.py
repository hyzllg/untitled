import pytest
from test_selenium.page.index import Index
from test_selenium.page.index import Login


class TestCase:
    # 对注册功能的测试
    def test_001(self):
        # 进入index，然后进入注册页填写信息
        print(Index().index())
    # 对login功能的测试
    # @pytest.mark.skip
    def test_002(self):
        # 从首页进入到注册页
        print(Login().login())


if __name__ == '__main__':
    pytest.main(['-vs','test_index.py::TestCase'])