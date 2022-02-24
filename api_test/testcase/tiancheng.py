import pytest
from page.request_func import api_requests
import conf



@pytest.mark.usefixtures('datas')
class Test_TianCheng:

    #甜橙授信申请接口
    @pytest.mark.usefixtures('set_global_data')
    def test_credit_granting(self,datas):
        result = api_requests(datas,'CREDIT_GRANTING',conf.sit_url)
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        assert '01'==result['data']['body']['status']
        self.set_global_data('creditApplyNo',result['data']['body']['creditApplyNo'])
        assert 1 ==self.get_global_data('creditApplyNo')

def main():
    pytest.main(['-vs', 'tiancheng.py::Test_TianCheng'])
if __name__ == '__main__':
    main()