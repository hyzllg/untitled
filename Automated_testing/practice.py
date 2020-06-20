from selenium import webdriver
driver = webdriver.Chrome()
url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
driver.get(url)
driver.find_element_by_name("accounts").send_keys('hyzllg')
driver.find_element_by_name("pwd").send_keys('1234567890')
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button").click()