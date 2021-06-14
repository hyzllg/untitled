from selenium import webdriver
from PIL import Image
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import Collect


#反监测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
#实例一个浏览器驱动
driver = webdriver.Chrome()
#浏览器窗口最大化
driver.maximize_window()
#访问12306登录页面
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
# #防止被12306识别为selenium登陆
# script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
# driver.execute_script(script)
# 实现规避selenium检测
script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
driver.execute_script(script)
#隐式等待
driver.implicitly_wait(10)
#获取登录页面句柄
search_windows = driver.current_window_handle
#使用账号密码登录
sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
sleep(1)
#定位到账号密码框并输入账号密码
driver.find_element_by_xpath('//input[@id="J-userName"]').send_keys("16621381003")
driver.find_element_by_xpath('//input[@id="J-password"]').send_keys("hyzllg336699")
while True:

    #获取验证码
    #第一步先将浏览器当前页面进行截图,保存hyzllg.png文件
    driver.save_screenshot('hyzllg.png')
    ##第二步将验证码进行局部截图，先利用location获取图片右上角坐标下x,y
    img_atg = driver.find_element_by_xpath('//*[@class="imgCode"]')
    #验证码左上角坐标，xy
    location = img_atg.location
    # print(location)
    #然后获取验证码的高和宽
    size = img_atg.size
    # print(size)
    # 用验证码左上角的xy加上验证码的高和宽，得出验证码右下角的xy
    # 因为电脑显示的缩放比例不同，默认是按照100%缩放比例获取坐标，所以应该将坐标乘以缩放比例
    rangle = (int(location['x'])*2,int(location['y'])*2,int(location['x']+size['width'])*2,int(location['y']+size['height'])*2)
    # print(rangle)
    #利用image crop进行局部截图
    img = Image.open('hyzllg.png')
    new_img = 'code.png'
    frame = img.crop(rangle)
    frame.save(new_img)
    #下一步处理验证码，利用超级鹰打码平台进行验证码识别,获取符合题目图片坐标
    result = Collect.chaojiyingdranformImgCode('code.png',9004)
    print(result)
    all_list = []
    if '|' in result[0]:
        list_1 = result[0].split('|')
        count_1 = len(list_1)
        for i in range(count_1):
            xy_list = []
            x = int(list_1[i].split(',')[0])
            y = int(list_1[i].split(',')[1])
            xy_list.append(x)
            xy_list.append(y)
            all_list.append(xy_list)
    else:
        x = result[0].split(',')[0]
        y = result[0].split(',')[1]
        xy_list = []
        xy_list.append(int(x))
        xy_list.append(int(y))
        all_list.append(xy_list)
    print(all_list)
    # 遍历列表，使用动作链对每一个列表元素对应的x,y指定的位置进行点击操作
    for l in all_list:
        x = l[0]/2
        y = l[1]/2
        print(x,y)
        # code_img_ele上面定位的验证码的位置
        img_atg = driver.find_element_by_xpath('//*[@class="imgCode"]')
        ActionChains(driver).move_to_element_with_offset(img_atg, x, y).click().perform()
        sleep(0.5)

    # print(Collect.error_chaojiying(result[1]))
    driver.find_element_by_xpath('//*[@id="J-login"]').click()
    try:
        el = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        if el.is_displayed():
            break
    except:
        sleep(2)
        print(Collect.error_chaojiying(result[1]))
        print("再次循环，进行验证！")

#滑动验证码
span = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
# 对div_tag进行滑动操作
action = ActionChains(driver)
# 点击长按指定的标签
action.click_and_hold(span).perform()
#向右滑动x轴400像素
action.drag_and_drop_by_offset(span, 400, 0).perform()
sleep(1)


#获得当前所有打开的窗口句柄
all_handles = driver.window_handles
#进入登录成功窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print(driver.title)

        # 点击提示弹窗的确定按钮
        # driver.find_element_by_xpath('//*[@id="pop_162363287377284897"]/div[2]/div[3]/a').click()
        # 切换到alert
        a = driver.switch_to_alert()
        # 打印弹出框文本内容
        print(a.text)
        sleep(2)
        # 点击确定
        a.accept()








