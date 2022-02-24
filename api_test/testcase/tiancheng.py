import pytest
from page.request_func import api_requests
import conf



@pytest.mark.usefixtures('datas')
class Test_TianCheng:


    #甜橙授信申请接口
    def test_credit_granting(self,datas,set_global_data):
        #调用甜橙授信申请信息接口，获取响应
        result = api_requests(datas,'CREDIT_GRANTING',conf.sit_url)
        #进行响应断言
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        assert '01'==result['data']['body']['status']
        #提取creditApplyNo用于授信结果查询接口
        set_global_data('creditApplyNo',result['data']['body']['creditApplyNo'])

    #因授信需要时间，顾授信查询接口设置成重跑16此，每次间隔3秒
    @pytest.mark.flaky(reruns=16, reruns_delay=3)#reruns代表重试次数，reruns_delay代表间隔时间
    def test_credit_inquiry(self,datas,get_global_data):
        #取出creditApplyNo
        creditApplyNo = get_global_data('creditApplyNo')
        #替换掉授信结果查询接口请求信息中的creditApplyNo
        datas['CREDIT_GRANTING']['res']['creditApplyNo'] = creditApplyNo
        # 调用甜橙授信申请结果查询接口，获取响应
        result = api_requests(datas,'CREDIT_INQUIRY',conf.sit_url)
        #进行响应断言
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        assert '01'==result['data']['body']['status']

    def test_disburse_trial(self,datas,set_global_data):
        # 调用甜橙支用试算接口，获取响应
        result = api_requests(datas,'DISBURSE_TRIAL',conf.sit_url)
        # 提取响应中的资方编码
        capitalCode = result['data']['body']['capitalCode']
        set_global_data('capitalCode',capitalCode)
        #进行响应断言
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        assert '01'==result['data']['body']['status']


def main():
    pytest.main(['-vs', 'tiancheng.py::Test_TianCheng'])
if __name__ == '__main__':
    main()