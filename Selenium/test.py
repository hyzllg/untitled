from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
#最大化显示
driver.maximize_window()
# 鼠标悬停至“设置”链接
driver.find_element_by_xpath('//*[@id="s-usersetting-top"]').click()
sleep(1)
# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# 搜索结果显示条数
sel = driver.find_element_by_xpath('//*[@id="nr_3"]')
Select(sel).select_by_value('50')  # 显示50条
# ……

driver.quit()