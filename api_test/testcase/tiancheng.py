import os

import pytest
from page.request_func import api_requests,rd_excle_data
import conf
import allure


@pytest.fixture(scope='class')
def datas():
    data = rd_excle_data('../datas/甜橙放款测试用例.xls')
    return data

@pytest.mark.usefixtures('datas')
@allure.feature("甜橙放款")
class Test_TianCheng:


    #甜橙授信申请接口
    @pytest.mark.run(order=1)
    @allure.story("甜橙授信接口")
    @allure.step("甜橙发起授信申请")
    def test_credit_granting(self,datas,set_global_data,LOG):
        LOG.info("调用甜橙授信接口")
        LOG.info(f"甜橙授信接口请求报文:{datas['CREDIT_GRANTING']['res']}")
        result = api_requests(datas,'CREDIT_GRANTING',conf.sit_url)
        LOG.info(f"甜橙授信接口响应报文:{result}")
        LOG.info("响应断言")
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        assert '01'==result['data']['body']['status']
        creditApplyNo = result['data']['body']['creditApplyNo']
        LOG.info(f"creditApplyNo : {creditApplyNo}")
        set_global_data('creditApplyNo',creditApplyNo)

    #因授信需要时间，顾授信查询接口设置成重跑16此，每次间隔3秒
    @pytest.mark.flaky(reruns=16, reruns_delay=3)  # reruns代表重试次数，reruns_delay代表间隔时间
    @pytest.mark.run(order=2)
    @allure.story("甜橙授信结果查询接口")
    @allure.step("甜橙发起授信结果查询")
    def test_credit_inquiry(self,datas,get_global_data,LOG):
        LOG.info("替换授信结果查询接口中的creditApplyNo")
        creditApplyNo = get_global_data('creditApplyNo')
        datas['CREDIT_INQUIRY']['res']['creditApplyNo'] = creditApplyNo
        LOG.info("调用甜橙授信结果查询接口")
        LOG.info(f"甜橙授信结果查询接口请求报文:{datas['CREDIT_INQUIRY']['res']}")
        result = api_requests(datas,'CREDIT_INQUIRY',conf.sit_url)
        LOG.info(f"甜橙授信结果查询接口响应报文:{result}")
        LOG.info("响应断言")
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        assert '01'==result['data']['body']['status']

    @pytest.mark.run(order=3)
    @allure.story("甜橙支用试算接口")
    @allure.step("甜橙发起支用试算")
    def test_disburse_trial(self,datas,set_global_data,LOG):
        LOG.info("调用甜橙支用试算接口")
        LOG.info(f"甜橙支用试算接口请求报文:{datas['DISBURSE_TRIAL']['res']}")
        result = api_requests(datas,'DISBURSE_TRIAL',conf.sit_url)
        LOG.info(f"甜橙使用试算接口响应报文:{result}")
        capitalCode = result['data']['body']['capitalCode']
        set_global_data('capitalCode',capitalCode)
        LOG.info(f"提取capitalCode : {capitalCode}")
        LOG.info("响应断言")
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        assert '01'==result['data']['body']['status']

    @pytest.mark.run(order=4)
    @allure.story("甜橙支用接口")
    @allure.step("甜橙发起支用")
    def test_disburse(self,datas,get_global_data,oracle_mate,LOG):
        sql = "update customer_info set liveaddress = '北京市市辖区东城区' where CERTID = '%s'" % datas['CREDIT_GRANTING']['res']['idNo']
        LOG.info(f"更新客户表信息: {sql}")
        oracle_mate.insert_update_data(sql)
        LOG.info(f"更新请求中的capitalCode: {get_global_data('capitalCode')}")
        capitalCode = get_global_data('capitalCode')
        datas['DISBURSE']['res']['capitalCode'] = capitalCode
        LOG.info("调用甜橙支用接口")
        LOG.info(f"甜橙支用接口请求报文:{datas['DISBURSE']['res']}")
        result = api_requests(datas,'DISBURSE',conf.sit_url)
        LOG.info(f"甜橙使用接口响应报文:{result}")
        LOG.info("响应断言")
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        assert '01'==result['data']['body']['status']


def main():
    pytest.main(['-v','-q', 'tiancheng.py' , '--clean-alluredir','--alluredir', '../allure_report_xml'])
    os.system('allure generate ../allure_report_xml -o ../allure_report_html --clean')
if __name__ == '__main__':
    main()
