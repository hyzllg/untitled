import requests
import sys
import yaml
import xlrd

book = xlrd.open_workbook('./文本审核接口测试用例.xls')
with open('../test_selenium/datas/datas.yaml','r',encoding='utf-8') as f:
    data = yaml.load(f,Loader=yaml.SafeLoader)
print(data)