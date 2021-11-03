import pytest

t = [1,2,3,4]
class Test_Class:
    @pytest.mark.parametrize('data',t)
    def test_01(self,data):
        print(f'第{data}条测试用例！')



if __name__ == '__main__':
    pytest.main(['-vs','test_ci.py::Test_Cless::test_01'])