from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time




driver = webdriver.Chrome()
# 规避浏览器selenium检测
with open('stealth.min.js', 'r') as f:
    js = f.read()
# 调用函数在页面加载前执行脚本
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})

#登录12306
driver.get("https://kyfw.12306.cn/otn/resources/login.html")
driver.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys("16621381003")
driver.find_element(By.XPATH,'//*[@id="J-password"]').send_keys("hyzllg336699")
driver.find_element(By.XPATH,'//*[@id="J-login"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@class="dzp-confirm"]/div[2]/div[3]/a').click()
driver.find_element(By.XPATH,'//*[@id="J-index"]/a').click()#首页
driver.find_element(By.XPATH,'//*[@id="fromStationText"]').clear()
driver.find_element(By.XPATH,'//*[@id="fromStationText"]').click()
driver.find_element(By.XPATH,'//*[@id="fromStationText"]').send_keys("上海")#出发地
driver.find_element(By.XPATH,'//*[@id="fromStationText"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//*[@id="toStationText"]').clear()
driver.find_element(By.XPATH,'//*[@id="toStationText"]').click()
driver.find_element(By.XPATH,'//*[@id="toStationText"]').send_keys("周口")#目的地
driver.find_element(By.XPATH,'//*[@id="toStationText"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//*[@id="train_date"]').clear()
driver.find_element(By.XPATH,'//*[@id="train_date"]').send_keys("2022-06-14")#出发日期
driver.find_element(By.XPATH,'//*[@id="train_date"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//*[@id="search_one"]').click()#查询
number = 1
time.sleep(2)
# driver.find_element(By.XPATH,f'//*[@id="queryLeftTable"]/tr[{number-1}]/td[13]/a').click()



'//*[@id="ticket_5q000G195203_04_11"]/td[13]/a'