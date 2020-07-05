from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

a = driver.find_element_by_xpath('//a[@name="tj_briicon"]')
ActionChains(driver).move_to_element(a).perform()