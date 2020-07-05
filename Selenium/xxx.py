from time import sleep
from selenium import webdriver

url = "http://www.126.com"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
current_frame = driver.find_element_by_xpath('//iframe[@scrolling="no"]')
driver.switch_to.frame(current_frame)
driver.find_element_by_xpath('//input[@data-loginname="loginEmail"]').send_keys("hyzllg")
driver.find_element_by_xpath('//input[@class="j-inputtext dlpwd"]').send_keys("123456789")
driver.find_element_by_xpath('//input[@id="un-login"]').click()
driver.switch_to.default_content()
driver.find_element_by_xpath('//a[@class="f-float-left"]').click()
current_windows = driver.current_window_handle
print(current_windows)
all_handles = driver.window_handles
print(all_handles)
for handle in all_handles:
    if handle != current_windows:
        driver.switch_to.window(handle)
        driver.find_element_by_xpath('//div[@class="custom-checkbox service"]/span').click()
        driver.find_element_by_xpath('//input[@class="username"]').send_keys("hyzllg")
        driver.find_element_by_xpath('//input[@class="password"]').send_keys("hyzllg33123456")
        driver.find_element_by_xpath('//input[@class="phone"]').send_keys("16635468545")
        driver.find_element_by_xpath('//a[@class="j-register"]').click()
        sleep(10)
        driver.close()
driver.switch_to.window(current_windows)

sleep(2)
