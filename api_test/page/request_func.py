import cx_Oracle
import requests
import xlrd
import json
from xlutils.copy import copy        #导入copy模块
from page import generate_customer_info
from ast import literal_eval
import conf




#生成默认请求信息
def default_data():
    res_dict = {}
    if not res_dict:
        idNo = generate_customer_info.customer().idNo()
        res_dict['idNo'] = idNo
        name = generate_customer_info.customer().name()
        res_dict['name'] = name
        phone = generate_customer_info.customer().phone()
        res_dict['phone'] = phone
        bankCard = generate_customer_info.customer().bankcard()
        res_dict['bankCard'] = bankCard
        channelCustId = generate_customer_info.customer().reqno(66)
        res_dict['channelCustId'] = channelCustId
        creditReqNo = generate_customer_info.customer().reqno(88)
        res_dict['creditReqNo'] = creditReqNo
        loanReqNo = generate_customer_info.customer().reqno(99)
        res_dict['loanReqNo'] = loanReqNo
        insuranceNo = generate_customer_info.customer().reqno(77)
        res_dict['insuranceNo'] = insuranceNo


        res_dict['loanReqNo'] = loanReqNo
        res_dict['repayAmount'] = "8000"
        res_dict['loanAmount'] = "3000"
        res_dict['periods'] = "6"
        res_dict['custType'] = "0"
        res_dict['capitalCode'] = conf.capitalCode
        res_dict['custGrde'] = "18"
    return res_dict

#读取excel测试用例
def rd_excle_data(path):
    wordbook = xlrd.open_workbook(path, formatting_info=True)#formatting_info=True表示保留原有格式
    table = wordbook.sheet_by_name('Sheet1')
    #获取整行内容
    rows_value = table.row_values(2)
    #获取整列内容
    cols_value = table.col_values(2)
    # 使用单元格定位
    cell_A1 = table.cell(2, 5).value
    # print(cell_A1)
    datas = {}
    #生成默认信息
    default = default_data()
    #取出数据放入datas列表中
    for i in range(2,table.nrows):
        datas[table.row_values(i)[2]] = {'url':table.row_values(i)[5],'method':table.row_values(i)[6],'res':fill_request(default,table.row_values(i)[7])}

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
    response = requests.request(datas[api_name]['method'],url=url+datas[api_name]['url'],headers=headers,data=json.dumps(datas[api_name]['res']))
    result = response.json()
    result["data"] = eval(result["data"])

    return result

def fill_request(default_dict,data):

    datas = data % default_dict
    #利用literal_eval将str转换成json格式
    return literal_eval(datas)




def oracle_conf(environment):
    if environment.upper() == 'SIT':
        _oracle_conf_xb = conf.xsxb_sit_oracle
        _oracle_conf_zw = conf.xxhx_sit_oracle
    elif environment.upper() == 'UAT':
        _oracle_conf_xb = conf.xsxb_uat_oracle
        _oracle_conf_zw = conf.xxhx_uat_oracle
    elif environment.upper() == 'DEV':
        _oracle_conf_xb = conf.xsxb_dev_oracle
        _oracle_conf_zw = conf.xxhx_sit_oracle
    else:
        print("传入参数错误，应为SIT UAT DEV")
    return _oracle_conf_xb,_oracle_conf_zw

#创建数据库操作类
class Oracle_Class:
    def __init__(self,user,passwd,listener):
        #创建数据库连接
        self.conn = cx_Oracle.connect(user, passwd, listener)
        #创建cursor
        self.cursor = self.conn.cursor()

    # 查询操作：一次性取所有数据。输入查询SQL，返回结果元组列表。
    def query_data(self, sql):
        list_result = []
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            list_result.append(row)
        return list_result

    # 支持对数据库的插入、更新和删除操作。输入操作SQL，无返回。
    def insert_update_data(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    #批量插入数据
    def batch_insert(self,masterplate,list_datas):
        #masterplate sql批量插入模版
        #list_datas 列表，里面放元组，每个元组里面放基于模版的对应数据
        self.cursor.prepare(masterplate)
        self.cursor.executemany(None, list_datas)
        self.conn.commit()

    # 关闭连接，释放资源
    def close_all(self):
        self.cursor.close()
        self.conn.close()

