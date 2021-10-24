import os
import pytest
from time import sleep
from selenium import webdriver
import Collect
import requests
import yaml
import xlrd
import json
import allure



def CustomerTrafficQueryService_api(data):
    url = 'http://10.1.14.123:27403/cfs-service/rest/services/customerTrafficQueryService'
    response = requests.post(url=url,data=json.dumps(data)).json()
    return response

file = open('CustomerTrafficQuery.yaml','r',encoding='utf-8')
datas = yaml.load(file,Loader=yaml.FullLoader)



@allure.epic("客户申请信息查询接口测试")
@allure.feature("正常场景")
class TestDemoAllure():
    #测试用例地址
    @allure.testcase("http://49.235.x.x:8080/zentao/testcase-view-6-1.html")
    #关联bug
    @allure.issue("http://49.235.x.x:8080/zentao/bug-view-1.html")
    #用例标题
    @allure.title("360投保信息接口name字段非空校验")
    @allure.story("用户故事：1")
    @allure.severity("critical")
    def test_case_1(self, driver_fixture):
        #用例描述
        '''
        1.点文章分类导航标签 -跳转编辑页面
        2.编辑页面输入，分类名称，如:上海-悠悠-可以输入
        3.点保存按钮保存成功
        '''
        #为这条用例添加附件
        file = open('git.txt', encoding='utf-8').read()
        allure.attach(name='cart_pay_err', body=file, attachment_type=allure.attachment_type.TEXT)




    #测试用例地址
    @allure.testcase("http://49.235.x.x:8080/zentao/testcase-view-6-1.html")
    #关联bug
    @allure.issue("http://49.235.x.x:8080/zentao/bug-view-1.html")
    @allure.title("360投保信息接口idno字段非空校验！")
    @allure.story("用户故事：2")
    def test_case_2(self, driver_fixture):
        #为这条用例添加附件
        file = open('git.txt', encoding='utf-8').read()
        allure.attach(name='cart_pay_err', body=file, attachment_type=allure.attachment_type.TEXT)




@allure.epic("0618版本接口测试用例")
@allure.feature("异常场景")
class TestDemo2():

    @allure.title("客服系统调用线上核心客户申请信息查询接口，线上核心返回对应客户对应的授信信息（未查询到该客户信息）")
    # @allure.story("用户故事：3")
    def test_case_3(self):
        '''
        1、客服系统调用线上核心客户申请信息查询接口
        2、查询不存在客户信息
        3、线上核心返回（未查询到该客户信息）
        '''
        file = open('git.txt', encoding='utf-8').read()
        allure.attach(name='cart_pay_err', body=file, attachment_type=allure.attachment_type.TEXT)
        datas['data1']['requestBody']['certId'] = Collect.id_card().generate_ID()
        result = CustomerTrafficQueryService_api(datas['data1'])
        assert result['responseHead']['appCode'] == "04"

    @allure.title("客服系统调用线上核心客户申请信息查询接口，线上核心返回对应客户对应的授信信息（身份证校验失败）")
    # @allure.story("用户故事：4")
    def test_case_4(self):
        '''
        1、客服系统调用线上核心客户申请信息查询接口
        2、查询身份证校验失败
        3、线上核心返回（身份证校验失败）
        '''
        file = open('git.txt', encoding='utf-8').read()
        allure.attach(name='cart_pay_err', body=file, attachment_type=allure.attachment_type.TEXT)
        result = CustomerTrafficQueryService_api(datas['data2'])
        assert result['responseHead']['appCode'] == "05"




if __name__ == '__main__':
    #--allure=./allure-results指定原始报告存放路径，--clean-alluredir生成新报告之前先删除旧报告
    pytest.main(['-vs','./CustomerTrafficQuery.py::TestDemo2','--alluredir=./allure-results','--clean-alluredir'])
    #命令行模式运行，先解析原始报告然后生成allure报告
    os.system("allure generate ./allure-results -c -o allure-report")
