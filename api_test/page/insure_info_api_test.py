import requests
import xlrd
import json
from xlutils.copy import copy        #导入copy模块


def rd_excle_data():
    wordbook = xlrd.open_workbook('../datas/文本审核接口测试用例.xls',formatting_info=True)#formatting_info=True表示保留原有格式
    table = wordbook.sheet_by_name('投保信息接口')
    #获取整行内容
    rows_value = table.row_values(2)
    #获取整列内容
    cols_value = table.col_values(2)
    # 使用单元格定位
    cell_A1 = table.cell(2, 5).value
    # print(cell_A1)
    datas = []
    for i in range(2,table.nrows):
        datas.append([table.row_values(i)[2],table.row_values(i)[4],table.row_values(i)[5],table.row_values(i)[6],table.row_values(i)[7]])
    return datas


def wd_excle_data(data):
    rb = xlrd.open_workbook('../datas/文本审核接口测试用例.xls')  # 打开xls文件
    wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet("投保信息接口")
    ws.write(int(data[0])+1, 8, str(data[1]))
    wb.save('../datas/文本审核接口测试用例-测试结果.xls')

def InsureInfo_request(data):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request(data[3],url=data[2],headers=headers,data=json.dumps(eval(data[4])))
    result = response.json()
    result["data"] = eval(result["data"])

    return result



