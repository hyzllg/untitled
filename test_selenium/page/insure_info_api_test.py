import requests
import xlrd
import json

def rd_excle_data():
    wordbook = xlrd.open_workbook('../datas/文本审核接口测试用例.xls')
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
def InsureInfo_request(data):
    response = requests.request(data[3],url=data[2],data=json.dumps(eval(data[4])))
    result = response.json()
    return result



