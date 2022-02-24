import requests
import xlrd
import json
from xlutils.copy import copy        #导入copy模块
import generate_customer_info


def rd_excle_data():
    wordbook = xlrd.open_workbook('../datas/甜橙放款测试用例.xls', formatting_info=True)#formatting_info=True表示保留原有格式
    table = wordbook.sheet_by_name('投保信息接口')
    #获取整行内容
    rows_value = table.row_values(2)
    #获取整列内容
    cols_value = table.col_values(2)
    # 使用单元格定位
    cell_A1 = table.cell(2, 5).value
    # print(cell_A1)
    datas = {}
    #取出数据放入datas列表中
    for i in range(2,table.nrows):
        # datas[table.row_values(i)[2]] = [table.row_values(i)[4],table.row_values(i)[5],table.row_values(i)[6],table.row_values(i)[7]]
        datas[table.row_values(i)[2]] = {'url':table.row_values(i)[5],'method':table.row_values(i)[6],'res':fill_request(table.row_values(i)[7])}

    return datas


def wd_excle_data(data):
    rb = xlrd.open_workbook('../datas/甜橙放款测试用例.xls')  # 打开xls文件
    wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet("投保信息接口")
    ws.write(int(data[0])+1, 8, str(data[1]))
    wb.save('../datas/文本审核接口测试用例-测试结果.xls')

def api_requests(datas,api_name,url):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request(datas[api_name]['method'],url=url+datas[api_name]['url'],headers=headers,data=json.dumps(eval(datas[api_name]['res'])))
    result = response.json()
    result["data"] = eval(result["data"])

    return result

def fill_request(data):
    res_dict = {}
    res_dict['idNo'] = generate_customer_info.customer().idNo()
    res_dict['name'] = generate_customer_info.customer().name()
    res_dict['phone'] = generate_customer_info.customer().phone()
    res_dict['bankCard'] = generate_customer_info.customer().bankcard()
    res_dict['channelCustId'] = generate_customer_info.customer().reqno(66)
    res_dict['creditReqNo'] = generate_customer_info.customer().reqno(88)
    res_dict['loanReqNo'] = generate_customer_info.customer().reqno(99)
    res_dict['repayAmount'] = "8000"
    res_dict['loanAmount'] = "3000"
    res_dict['periods'] = "6"
    res_dict['custType'] = "0"
    return data % res_dict

import conf
result = api_requests(rd_excle_data(),'CREDIT_GRANTING',conf.sit_url)
print(result)
print(type(result))