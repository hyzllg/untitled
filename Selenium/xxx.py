from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()
#隐式等待10秒
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
#获得百度窗口句柄
search_windows = driver.current_window_handle
a = driver.find_element_by_xpath('//a[@name="tj_briicon"]')
sleep(1)
#悬停操作
ActionChains(driver).move_to_element(a).perform()
sleep(1)
b = driver.find_element_by_xpath('//img[@src="https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/yinyue@2x-c18adacacb.png"]')
b.click()
sleep(1)

#切换窗口
#获得当前所有打开的窗口句柄
all_handles = driver.window_handles

#进入音乐窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        driver.find_element_by_xpath('//input[@id="kw"]').send_keys("月光")
        driver.find_element_by_xpath('//input[@id="kw"]').send_keys(Keys.ENTER)
        sleep(1)
        driver.close()
driver.switch_to.window(search_windows)
driver.title
driver.quit()





