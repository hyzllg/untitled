import pytest



class Test01:
    @pytest.mark.smock
    def test001(self,fixture):
        print(f"这是第一个用例!{fixture}")
        assert fixture == 666 , "校验fixtrue是否等于666"
    @pytest.mark.smock
    @pytest.mark.skip
    def test002(self):
        print("这是第二个用例！")



if __name__ == '__main__':
    pytest.main(['-v','-s','-q','test001.py::Test01','-m','smock','--html=./report/reprot.html --self-contained-html'],)