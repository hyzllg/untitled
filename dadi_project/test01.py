import time

import xlrd
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
# option = webdriver.ChromeOptions()
# option.add_argument("headless")
# driver = webdriver.Chrome(chrome_options=option)
driver = webdriver.Chrome()
#哔哩哔哩
driver.get('https://passport.bilibili.com/login')
#等待
driver.implicitly_wait(10)
#输入账号
driver.find_element(By.ID,'login-username').send_keys(16621381003)
#输入密码
driver.find_element(By.ID,'login-passwd').send_keys('hyzllg336699')
#点击登录
driver.find_element(By.XPATH,'//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
#强制等待，手动过验证
time.sleep(6)






