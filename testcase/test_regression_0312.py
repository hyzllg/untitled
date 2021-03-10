import pytest

@pytest.fixture(scope="function")
def my_fixture():
    print("前后置")

class Test_regression:
    def test001(self,my_fixture):
        print("这是第一条用例！")


if __name__ == '__main__':
    pytest.main(['test_regression_0312.py::Test_regression::test001'])