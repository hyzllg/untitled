import pytest
import requests
import xlrd
import json

book = xlrd.open_workbook('./1111.xlsx')
sheet1 = book.sheets()[0]
# print(sheet1.nrows)
datas_list = []
new_datas_list = []
for i in range(1,sheet1.nrows):

    data = sheet1.row_values(i)[1]
    data = data.replace('\n','').replace(' ','')
    datas_list.append(data)

for i in datas_list:
    data = json.loads(i,strict=False)
    new_datas_list.append(data)

print(new_datas_list)




# def get_func(data):
#     url = 'http://10.1.14.106:27405/channel/apitest/QFIN/INSURE_INFO'
#     response = requests.post(url,data=json.dumps(data))
#     page = response.json()
#     page['data'] = eval(page['data'])
#
#     return page['data']['code']
# # get_func(new_datas_list[0])
#
#
#
# class Testinsureinfo:
#     def test01(self):
#         data = get_func(new_datas_list[0])
#         assert data == '0001'
#
#     def test02(self):
#         data = get_func(new_datas_list[1])
#         assert data == '0001'
#
#
#
#
# if __name__ == '__main__':
#
#     pytest.main(['-vs','./test_api.py::Testinsureinfo'])