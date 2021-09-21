import pytest
import yaml
from test_selenium.page.index import Index
from page.get_ApiContentCensor_token import get_apicontentcensor_token


@pytest.fixture(scope="class")
def get_token():
    return get_apicontentcensor_token()

class TestCase:
    with open('./datas.yaml','r',encoding='utf-8') as f:
        texts = yaml.load(f,Loader=yaml.SafeLoader)
    @pytest.mark.parametrize("text",texts)
    def test_001(self,get_token,text):
        res = Index().index(get_token,text)
        print(res)
        assert res == "合规"

if __name__ == '__main__':
    pytest.main(['-vs','test_index.py::TestCase'])
