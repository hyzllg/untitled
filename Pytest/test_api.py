import pytest
import requests
import xlrd
import json

book = xlrd.open_workbook('360投保资料接口自动化测试用例.xlsx')
sheet1 = book.sheets()[0]
# print(sheet1.nrows)
datas_list = []
for i in range(1,sheet1.nrows):

    data = sheet1.row_values(i)[1]
    data = data.replace('\n','').replace(' ','')
    datas_list.append(json.loads(data))






def get_func(data):
    url = 'http://10.1.14.106:27405/channel/apitest/QFIN/INSURE_INFO'
    response = requests.post(url,data=json.dumps(data))
    page = response.json()
    page['data'] = eval(page['data'])

    return page['data']['code']
# get_func(new_datas_list[0])



class Testinsureinfo:
    def test01(self):
        data = get_func(datas_list[0])
        assert data == '0001',"非空校验"
    def test02(self):
        data = get_func(datas_list[1])
        assert data == '0001',"非空校验"
    def test03(self):
        data = get_func(datas_list[2])
        assert data == '0001',"非空校验"
    def test04(self):
        data = get_func(datas_list[3])
        assert data == '0001',"非空校验"
    def test05(self):
        data = get_func(datas_list[4])
        assert data == '0001',"非空校验"
    def test06(self):
        data = get_func(datas_list[5])
        assert data == '0001',"非空校验"
    def test07(self):
        data = get_func(datas_list[6])
        assert data == '0001',"非空校验"
    def test08(self):
        data = get_func(datas_list[7])
        assert data == '0001',"非空校验"
    def test09(self):
        data = get_func(datas_list[8])
        assert data == '0001',"非空校验"
    def test10(self):
        data = get_func(datas_list[9])
        assert data == '0001',"非空校验"
    def test11(self):
        data = get_func(datas_list[10])
        assert data == '0001',"非空校验"
    def test12(self):
        data = get_func(datas_list[11])
        assert data == '0001',"非空校验"
    def test13(self):
        data = get_func(datas_list[12])
        assert data == '0001',"非空校验"




if __name__ == '__main__':

    pytest.main(['-vs','./test_api.py::Testinsureinfo','--html=./report/report.html'])