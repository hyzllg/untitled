from selenium import webdriver
from time import sleep


#创建谷歌浏览器驱动对象
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

#浏览器窗口最大化
driver.maximize_window()

#隐式等待 等待页面元素全部加载
driver.implicitly_wait(10)
#设置按钮
driver.find_element_by_xpath('//span[@id="s-usersetting-top"]').click()
#搜索设置
driver.find_element_by_xpath('//a[@class="setpref"]').click()
# #多表单切换
# iframe = driver.find_element_by_xpath('/html/head/style[12]')
# driver.switch_to.frame(iframe)
#设置仅简体中文
driver.find_element_by_xpath('//*[@id="SL_1"]').click()
#设置每页显示20条搜索数据
driver.find_element_by_xpath('//input[@id="nr_2"]').click()
#保存设置
driver.find_element_by_xpath('//div[@id="se-setting-7"]/a[2]').click()
#点击保存会有弹窗提示
#切换到弹窗
alerts = driver.switch_to.alert
#打印弹窗内容
print(alerts.text)
sleep(2)
#接受同意框
alerts.accept()
sleep(2)
driver.quit()




