from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://landing.zhaopin.com/")
#获取当前窗口句柄
serch_windows = browser.current_window_handle
#刷新浏览器
browser.refresh()
#最大化显示
browser.maximize_window()
#登录 定位到手机号输入框
browser.find_element_by_xpath('//*[@class="carouselPassportWidget"]/div/div/div[2]/a-input-phone/div/input').send_keys(16621381003)
#点击或如验证码
browser.find_element_by_xpath('//*[@class="carouselPassportWidget"]/div/div/div[3]/button').click()
#手动输入收到的验证码
number = int(input("请输入验证码："))
time.sleep(5)

#填入验证码
browser.find_element_by_xpath('//*[@class="carouselPassportWidget"]/div/div/div[3]/a-input/input').send_keys(number)
#dianji我同意协议
browser.find_element_by_xpath('//*[@id="accept"]').click()
#点击注册/登录按钮
browser.find_element_by_xpath('//*[@class="carouselPassportWidget"]/div/div/button').click()
#隐式等待10秒
browser.implicitly_wait(10)
#定位到输入框
browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div[1]/input').send_keys("软件测试工程师")
#点击搜索
browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/button').click()

#获取当前所有打开窗口句柄
all_handles = browser.window_handles
for handle in all_handles:
    if handle != serch_windows:
        browser.switch_to.window(handle)
        print(browser.title)
        # print(browser.)

