from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome()
driver.get('chrome://version/')
driver.implicitly_wait(10)
version = driver.find_element_by_xpath('//*[@id="copy-content"]/span[1]').text
print(version)
driver.quit()
