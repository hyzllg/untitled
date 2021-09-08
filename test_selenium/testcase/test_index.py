import pytest
from test_selenium.page.index import Index
from test_selenium.page.index import Login
from page.get_ApiContentCensor_token import get_apicontentcensor_token


@pytest.fixture(scope="class")
def get_token():
    return get_apicontentcensor_token()

class TestCase:
    def test_001(self,get_token):
        text = "我喜欢你！"
        res = Index().index(get_token,text)
        print(res)
        assert res == "合规"
    # @pytest.mark.skip
    def test_002(self,get_token):
        text = "我讨厌你！"
        res = Index().index(get_token,text)
        print(res)
        assert res == "合规"
    def test_003(self,get_token):
        text = "尼玛"
        res = Index().index(get_token,text)
        print(res)
        assert res != "合规"


if __name__ == '__main__':
    pytest.main(['-vs','test_index.py::TestCase'])