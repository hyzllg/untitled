import yaml
import os
import cx_Oracle
import logging
from utils import database_manipulation,my_log
from selenium.webdriver.common.by import By
from selenium import webdriver




'''
第一步：
    创建日志器
        logger = logging.getloger()
第二步：
    创建处理器
        console_handler = logging.StreamHandler()
第三步：
    设置格式器
    fmt = logging.Formatter()
    处理器中加入格式
    console_handler.setFormatter(fmt)
#第四步：
    日志器添加处理器
    logger.addHandler()

'''
'''
path = './conf/Config.yaml'
datas = lambda path : yaml.load(open(path,mode='r',encoding='utf-8'),Loader=yaml.SafeLoader)
oracle_conf = datas(path)['xshx_oracle']['xsxb_sit_oracle']
conn = cx_Oracle.connect(oracle_conf[0],oracle_conf[1],oracle_conf[2])
cursor = conn.cursor()
sql = "select * from customer_info where customerid='320000001233778'"
cursor.execute(sql)
query_datas = cursor.fetchall()
conn.close()
if query_datas:
    print("True")
else:
    print("False")

'''

logger = logging.getLogger()
logger.setLevel(logging.INFO)
consule_handler = logging.StreamHandler()
fmt = logging.Formatter("%(asctime)s")
consule_handler.setFormatter(fmt)
logger.addHandler(consule_handler)

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
print(driver.current_url)
print(driver.current_window_handle)