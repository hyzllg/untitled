import os
import pytest
from page.request_func import api_requests,rd_excle_data
import conf
import allure
import re

@pytest.fixture(scope='class')
def datas():
    data = rd_excle_data('../datas/还呗放款测试用例.xls')
    return data


@pytest.mark.usefixtures('datas')
@allure.feature('还呗放款')
class Test_HuanBei:

    @pytest.mark.run(order=1)
    @allure.story('还呗投保信息接口')
    @allure.step('调用投保信息接口，提取token')
    def test_insure_info(self,datas,set_global_data,get_global_data,LOG):
        LOG.info('调用还呗投保信息接口')
        LOG.info(f"还呗投保信息接口请求报文:{datas['INSURE_INFO']['res']}")
        result = api_requests(datas,'INSURE_INFO',conf.sit_url)
        LOG.info(f"还呗投保信息接口响应报文:{result}")
        LOG.info('响应断言')
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        token = (re.search("lp=(.*)", result["data"]["insurAgencyUrl"])).group()[3:]
        LOG.info(f"提取token: {token}")
        set_global_data('token',token)

    @pytest.mark.run(order=2)
    @allure.story('还呗投保资料查询')
    @allure.step('调用投保资料查询接口，取出premiumRate用于投保接口')
    def test_insure_data_query(self,datas,get_global_data,set_global_data,LOG):
        LOG.info("替换请求中的token")
        datas['INSURE_DATA_QUERY']['res']["token"] = get_global_data('token')
        LOG.info('调用还呗投保资料查询接口')
        LOG.info(f"还呗投保资料查询接口请求报文:{datas['INSURE_DATA_QUERY']['res']}")
        result = api_requests(datas,'INSURE_DATA_QUERY',conf.sit_url)
        LOG.info(f"还呗投保资料查询接口响应报文:{result}")
        LOG.info('响应断言')
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        premiumRate = result["data"]["premiumRate"]
        LOG.info(f"提取月保费率: {premiumRate}")
        set_global_data('premiumRate',premiumRate)

    @pytest.mark.run(order=3)
    @allure.story('还呗投保')
    @allure.step('调用投保接口')
    def test_insure(self,datas,get_global_data,LOG):
        LOG.info(f"更新请求报文中的月保费率: {get_global_data('premiumRate')}")
        datas['INSURE']['res']["premiumRate"] = get_global_data('premiumRate')
        LOG.info('调用还呗投保接口')
        LOG.info(f"还呗投保接口请求报文:{datas['INSURE']['res']}")
        result = api_requests(datas,'INSURE',conf.sit_url)
        LOG.info(f"还呗投保接口响应报文:{result}")
        LOG.info('响应断言')
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        assert '01'==result['data']['status']

    @pytest.mark.run(order=4)
    @allure.story('还呗支用')
    @allure.step('调用支用接口')
    def test_disburse(self,datas,LOG):
        LOG.info('调用还呗支用接口')
        LOG.info(f"还呗支用请求报文:{datas['DISBURSE']['res']}")
        result = api_requests(datas,'DISBURSE',conf.sit_url)
        LOG.info(f"还呗支用接口响应报文:{result}")
        LOG.info('响应断言')
        assert True==result['result']
        assert 200==result['code']
        assert 'SUCCESS!'==result['msg']
        assert '01'==result['data']['status']

def main():
    pytest.main(['-v','-q', 'huanbei.py' , '--clean-alluredir','--alluredir', '../allure_report_xml'])
    os.system('allure generate ../allure_report_xml -o ../allure_report_html --clean')
if __name__ == '__main__':
    main()

