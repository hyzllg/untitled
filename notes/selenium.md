# selenium

## WebDriver API

### 1.1 定位元素

+ id定位    find_element_by_id()
+ name定位   find_element_by_name()
+ tag定位   find_element_by_tag_name()
+ class定位   find_element_by_class_name()
+ link_text定位   find_element_by_link_text()
+ partial link定位   find_element_by_partial_link_text()
+ XPath定位   find_element_by_id_xpath()
+ CSS_selector定位   find_element_by_css_selector()

### 1.2 控制浏览器

+ 控制浏览器大小   set_window_size()
+ 浏览器最大化   maximize_window()
+ 浏览器前进   forward()
+ 浏览器后退   back()
+ 浏览器刷新   refresh()

### 1.3 webdriver中常用方法

+ 清除文本   clear()
+ 模拟按键输入   send_keys(value)
+ 单击元素   click()
+ 提交表单   submit()
+ 返回元素的尺寸   size
+ 获取元素的文本   text
+ 获得属性值   get_attribute(name)
+ 设置该元素是否用户可见   is_displayed()

### 1.4 鼠标操作

在webdriver中，与鼠标操作相关的方法都封装在ActionChains类中

ActionChinas类提供了鼠标操作的常用方法：

+ perform()   :   执行ActionChains类中存储的所有行为
+ context_click()   :   右击
+ double_click()   :   双击
+ drag_and_drop()   :   拖动
+ move_to_element()   :   鼠标悬停

例：

​    ActionChains(driver).move_to_element(hyz).perform()

### 1.5 键盘操作

在使用键盘按键方法前需要导入Keys类

from selenium.webdriver.common.keys import Keys

常用键盘操作：

+ send_keys(Keys.BACK_SOACE) : 删除键（Backspace）
+ send_keys(Key.SPACE) : 空格键（Space）
+ send_keys(Key.TAB) : 制表符（Tab）
+ send_keys(Keys.ESCAPE) : 回退键（Esc）
+ send_keys(Keys.ENTER) : 回车键（Enter）
+ send_keys(Keys.CONTROL,'a') : 全选（Ctrl+a）
+ send_keys(Keys.CONTROL,'c') : 复制（Ctrl+c）
+ send_keys(Keys.CONTROL,'x') : 剪切（Ctrl+x）
+ send_keys(Keys.CONTROL,'v') : 粘贴（Ctrl+v）
+ send_keys(Keys.F1~F12)

### 1.6 获得验证信息

在进行Web自动化测试中，用的最多的集中验证信息是title，current_url和text

+ title : 用于获取当前页面的标题
+ current_url : 用于获取当前页面的URL
+ text ：用于获取当前页面的文本信息

### 1.7 设置元素等待

webdriver提供了两种类型的元素等待：显式等待和隐式等待

#### 1.7.1 显式等待

​	显式等待是Webdriver等待某个条件成立则继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）

​	WevDriverWait类是Wevdriver提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间仍检测不到，则抛出异常。

​	WevDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)

+ driver ：浏览器驱动

+ timeout ：最长超时时间，默认以秒为单位

+ poll_frequency：检测的间隔时间，默认为0.5秒

+ ignored_exceptions：超时后的异常信息，默认情况下抛出NoSuchElementException异常

  Webdriverwait()一般与until()或until_not()方法配合使用，下面是until()和until_not()方法的说明

  + until(method,message='')

  调用该方法提供的驱动程序作为一个参数，直到返回值为True

  + until_not(method,message='')

  调用该方法提供的驱动程序作为一个参数，直到返回值为False

例：

```python
from selenium import webdriver
from selenium import webdriver.common.by import By
from selenium.webdriver.suport.ui import WebDriverWait
from selenium.webdriver.suport import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("htts://www.baidu.com/")
element = WebDriverWait(driver,5,0.5).until(
 EC.visibility_of_element_located((By.ID,"kw")))
element.send_keys('selenium')
driver.quit()
```

​	本例中，通过as关键字将expected_conditions重命名为EC，并调用presence_of_element_located()方法判断元素是否存在

```python
title_is #判断当前页面的标题是否等于预期
title_contains #判断当前页面的标题是否包含预期字符串
presence_of_element_located #判断元素是否被加在DMO树里，并不代表该元素一定可见
visibility_of_element_located #判断元素是否可见（可见代表元素非隐藏，并且元素的宽和高等都不等于0
visibility_of #与上一个方法作用相同，上一个方法的参数为定位，该方法接收的参数为定位后的元素
presence_of_all_element_located #判断是否至少有一个元素存在于DOM树中。例如，在页面中有个n个元素的class为“wp”，那么只要有一个元素存在于DOM树中就返回True
text_to_be_present_in_element #判断某个元素中的text是否包含预期的字符串
text_to_be_present_in_element_value #判断某个元素的value属性是否包含预期的字符串
frame_to_be_available_and_switch_to_it #判断该表单是否可以切换进去，如果可以，返回True并且切换进去，否则返回Falue
invisibility_of_element_located #判断某个元素是否不在DOM树中或不可见
element_to_be_clickable #判断某个元素是否可见并且是可以点击的
element_to_be_selected #判断某个元素是否被选中，一般用在下拉列表中
element_selection_state_to_be #判断某个元素的选中状态是否符合预期
staleness_of #等到一个元素从DOM树中移除
element_located_selection_state_to_be #与上一个方法作用相同，只是一个方法参数为定位后的元素，该方法接收的参数为定位
alert_is_present #判断页面上是否存在alert

```

​	除expected——conditions类提供的丰富的预期条件判断方法外，还可以利用前面学到的is_displayed()方法自己实现元素显式等待。

​	

```python
for i in range(10):
    try:
        el = driver.find_element_by_id("kw32")
        if el.is_displayed():
            break
    except:
        pass
    sleep(1)
else:
    print("time out")
driver.quit()
```

​	相对来说，这种方式更容易理解。首先for循环10次，然后通过is_displayed()方法循环判断元素是否可见。如果为True，则说明元素可见，执行break跳出循环；否则执行sleep()休眠1s继续循环判断。10次循环结束后，如果没有执行break，则执行for循环对应的else语句，打印“time out”信息。

#### 1.7.2 隐式等待

WebDriver提供了implicitly_wait()方法可以用来实现隐式等地，用方法来说要简单的多。

```python
from time import ctime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
#设置为隐式等待为10s
driver.implicitly_wait(10)
driver.get()
try:
    print(ctime)
    driver.find_element_by_id("kw32").send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime)
    driver.quit()
```

​	implicitly_wait()的参数是时间，单位为秒，本例中设置的等待时间是10s。首先，这10s并非一个固定的等待时间，它并不影响脚本的执行速度。其次，它会等待页面上的所有元素。当脚本执行到某个元素定位时，如果元素存在，则继续运行；如果定位不到元素，则它将进行轮询的方式不断地判断元素是否存在。假设在第6s定位到了元素，则继续运行，若直到超出设置时间还没有定位到元素，则抛出异常。

### 1.8 定位一组元素

WebDriver还提供了8种用于定位一组元素的方法：

定位一组元素的方法与定位单个元素的方法非常像，唯一的区别是单词“element”后面多了个“s”，用来表示复数。

运行结果：

### 1.9 多表单切换

​		在Web应用中经常会遇到frame/iframe表单嵌套页面的应用，WebDriver只能在一个页面上对元素进行识别和定位，无法直接定位frame/iframe表单内嵌页面上的元素，这时就需要通过swich_to.frame()方法将当前定位的主体切换为frame/iframe表单的内嵌页面。

```python
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get()
sleep(2)
login_frame = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to.frame(login_frame)
driver.switch_to.default_content()
```

​		switch_to.frame()默认可以直接对表单的id属性或name属性传参，因而可以定位元素的对象。在这个例子中，表单的id属性后半部分的数字（1553484417298.5217）是随机变化的，在CSS定位方法中，可以通过“^=“匹配id属性为以”x-URS-iframe"开头的元素。

​		最后，通过swith_to.default_content()回到最外层的页面。

### 1.10 多窗口切换

​		在页面操作过程中，有时单击某个链接会弹出新的窗口，这时就需要切换到新打开的窗口中进行操作。WevDriver提供的switch_to.window()方法可以实现在不同的窗口间切换。

+ current_window_handle:获得当前窗口句柄

+ window_handles:返回所有窗口的句柄到当前会话

+ switch_to.window():切换到相应的窗口

  ​	以百度首页和账号注册页为例，在两个窗口之间的切换
  
  ```python
  import time 
  from selenium import webdriver
  
  driver = webdriver.Chrome()
  driver.implicitly_wait(10)
  driver.get("https://www.baidu.com")
  #获得百度搜索窗口句柄
  search_windows = driver.current_window_handle
  driver.find_element_by_link_text('登录').click()
  driver.find_element_bye_link_text('立即注册').click()
  #获得当前所有打开的窗口句柄
  all_handles = driver.windows_handles
  #进入注册窗口
  for handle in all_handles:
      if handle != search_windows:
          driver.switch_to.window(handle)
          print(driver.title)
          driver.find_element_by_name('userName').send_keys('username')
          driver.find_element_by_name('phone').send_keys('phone')
          time.sleep(2)
          #关闭当前窗口
          driver.close()
  #回到搜索窗口
  driver.switch_to.window(search_windows)
  print(driver.title)
  driver.quit()
  ```

​		脚本的执行过程：首先打开百度首页，通过current_window_handle获得当前窗口句柄，并赋值给变量search_handle。接着打开登陆窗口，在登录弹窗上单击“立即注册”链接，从而打开新的注册窗口。通过window_handles获得当前所有窗口句柄（包含百度首页和账号注册页），并赋值给变量all_handles。

​		循环遍历all_handles，如果handle不等于search_handles,那么一定是注册窗口，因为在脚本执行过程中只打开了两个窗口。然后，通过switch_to.window()切换到账号注册页。

### 1.11 警告框处理

​		在WebDriver中处理JavaScript生成的alert、confirm和prompt十分简单，具体做法是，首先使用switch_to.alert()方法定位，然后使用text、accept、dismiss、send_keys等进行操作。

+ text：返回alert、confirm、prompt中的文字信息

+ accept（）：接受现有警告框

+ dismiss（）：解散现有警告框

+ send_keys()：在警告框中输入文本（如果可以输入的话）

  可以使用switch_to.alert()方法为百度搜索设置弹窗
  
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.action_chains import ActionChains #导入鼠标操作
  from selenium.webdriver.common.keys import Keys #导入键盘操作
  
  driver=webdriver.Firefox()
  
  driver.get("https://www.baidu.com")
  
  mouse=driver.find_element_by_link_text("设置")
  
  ActionChains(driver).move_to_element(mouse).perform() #鼠标悬浮在 设置上
  
  driver.find_element_by_link_text("搜索设置").click()
  
  dd=driver.find_element_by_class_name("prefpanelgo") #保存设置按钮
  
  dd.send_keys(Keys.ENTER) #鼠标回车
  
  ale=driver.switch_to.alert # 通过switch_to.alert切换到alert
  
  ale.accept()
  
  #ale=driver.switch_to_alert().accept() #老写法
  
  driver.close()
  ```
  
  

​		这里以百度搜索设置为例，打开百度瞍索设置，设置完成后单击“保存设置”按钮，弹出保存确认警告框。通过switch_to.alert获取当前页面上的警告框，text用于获取警告框提示信息，accept()于接受警告框。

### 1.12 下拉框处理

​		下拉框是Web页面常见功能之一，WebDriver提供了Select类来处理下拉框：

+ Select类：用于定位<select>标签

+ select_by_value()：通过value值定位下拉选项

+ select_by_visible_text()：通过text值定位下拉选项

+ select_by_index()：根据下拉选项的索引进行选择。第一个选项为0，第二个选项为1

  以百度搜索设置为例，下拉框代码如下：

  ```html
<select name="NR" id="nr">
      <option value="10" selected="">每页显示10条</option>
    <option value="20">每页显示20条</option>
      <option value="50">每页显示50条</option>
</select>
  ```
  
  通过WevDriver代码操作下拉框：
  
  ```python
  from time import sleep
  from selenium import webdriver
  from selenium.webdriver.support.select import Select
  
  driver = webdriver.Chome()
  driver.get("https://www.baidu.com")
  
  #打开搜索设置
  link = driver.find_element_by_link_text('设置').click()
  driver.find_element_by_link_text("搜索设置").click()
  sleep(2)
  #搜索结果显示条数
  sel = driver.find_element_by_xpath("//select[@id='nr']")
  # value="20"
  Select(sel).select_by_value('20')
  sleep(2)
  #<option>每页显示50条</option>
  Select(sel).select_by_visible_text("每页显示50条")
  sleep(2)
  #根据下拉选项的索引进行选项
  Select(sel).select_by_index(0)
  sleep(2)
  
  driver.quit()
  ```

### 1.13 上传文件

​		上传文件是比较常见的Web功能之一，但WebDriver并没有提供专门用于上传的方法，实现文件上传的关键在于思路。

​		在Web页面中，文件上传操作一般需要单击"上传"按钮后打开本地wndows窗囗，从窗囗中选择本地文件进行上传。因为WebDriver无法操作Wndows控件，所以对于初学者来说，一般思路会卡在如何识别wndows控件这个问题上。

​			在web页面中一般通过以下两种方式实现文件上传：

+ 普通上传：将本地文件路径作为一个值放在input标签中，通过form表单将这个值提交给服务器。

+ 插件上传：一般是指基于FIash、JavaScript或Ajax等技术实现的上传功能。

  ​	对于通过input标签实现的上传功能，可以将其看作一个输入框，即通过send_keys()指定本地文件路径的方式实现文件上传。
  
  ```python
  import os
  from selenium import webdriver
  file_path = os.path.abspath('./files/')
  driver = webdriver.Chrome()
  upload_page = 'file:///' + file_path + 'upfile.html'
  driver.get(upload_page)
  #定位上传按钮，添加本地文件
  driver.find_element_by_id("file").send_keys(file_path + 'test.txt')
  ```

​		这里测试的页面（upfile.html）和上传的文件（test.txt）位于与当前程序同目录的files/目录下

​		通过这种方式上传，就避免了操作Windows控件。如果能找到上传的input标签，那么基本可以通过send_keys()方法输入一个本地文件路径实现上传

​		对于插件上传，我们可以使用Autolt来实现

### 1.14 下载文件

​		Webdriver允许我们设置默认的文件下载路径，也就是说，文件会自动下载并且存放到设置的目录中，不同的浏览器设置方式不同。

下面以Chrome浏览器为例，演示文件的下载。

```python
import os 
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,
        'download.default_directory': os.getcwd()}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://pypi.org/project/seleium/#files")
driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()
```

Chrome浏览器在下载时默认不会弹出下载窗口，这里主要想修改默认的下载路径。

```python
profile.default_content_settings.popups
```

设置为0，表示禁止弹出下载窗口

```python
download.default_directory
```

设置文件下载路径，使用os.getcwd()方法获取当前脚本的目录作为下载文件的保存位置

### 1.15 操作Cookie

​		有时我们需要验证浏览器中的Cookie是否正确，因为基于真实的Cookie时无法通过白盒测试和集成测试的。WevDriver提供了操作Cookie的相关方法，可以读取、添加和删除Cookie。

​		WebDriver操纵Cookie的方法如下：

+ get_cookies()：获得所有的Cookie

+ get_cookie(name)：返回字典中key为”name“的Cookie

+ add_cookie(cookie_dict)：添加Cookie

+ delete_cookie(name,optionsString)：删除名为OpenString的Cookie

+ delete_all_cookies()：删除所有Cookie

  下面通过get_cookies()获取当前浏览器的所有Cookie

  ```python
from selenium import webdriver
  driver = webdriver.Chrome()
driver.get("https://www.baicu.com")
  #获得所有Cookie信息并打印
cookies = driver.get_cookies()
  print(cookies)
  ```

​        可以看出，Cookie中的数据时以字典形式存放的。知道了Cookie中数据的存放形式后，即可按照这种形式向浏览器中添加Cookie

```python
#添加Cookie信息
driver.add_cookie({'name':'key-aaaaaa'},'value':'value-bbbbbb')
#遍历指定的Cookies
for cookie in driver.get_cookies():
	print("%s -> %s" % (cookie['name'],cookie['value']))
```

​		可以看出，最后一条Cookie是在脚本执行过程中通过add_cookie()方法添加的。通过遍历得到所有的Cookie，从而找到字典中key为”name“和”value”的Cookie值。

​		delete_cookie()和delete_all_cookies()方法的使用也很简单，前者通过name删除一个指定的Cookie，后者直接删除浏览器中的所有Cookies。

### 1.18 滑动解锁

​		滑动解锁:

​		slide-to-unlock-handle表示滑块。在滑动过程中，滑块的左边距离会逐渐变大，因为它在向右移动。

​		slide-to-unlock-progress表示滑过之后的背景色，背景色的区域会逐渐增加，因为滑块在向右移动。

```python
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.get("https://www.helloweba.com/deme/2017/unlock/")

#定位滑动模块
slider = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]
action = ActionChains(driver)
action.click_and_hold(slider).perform()

for index in range(200):
	try:
        action.move_by_offset(2,0).perform()
    except UnexpectedAlertPresentException:
        break
    action.reset_actions()
    sleep(0.1)
    
#打印警告框提示
success_text = driver.switch_to.alert.text
print(success_text)
```

​		在这个脚本中，用到下面几个方法：

+ click_and_hold()：单击并按下鼠标左键，在鼠标事件中介绍过
+ move_by_offset()：移动鼠标，第一个参数为x坐标距离，第二个参数为y坐标距离
+ reset_action()：重置action

​		参考前面的操作，通过ActionChains类可以实现上下滑动选择日期，但是这里要介绍另外一种方法，及通过TouchActions类实现上下滑动选择日期。

```python
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.jq22.com/yanshi4976")
sleep(2)
driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()
#定位要滑动的年、月、日
dwwos = driver.find_elements_by_class_name("dwwo")
year = dwwos[0]
month = dwwos[1]
day = dwwos[2]
action = webdriver.TouchActions(driver)
action.scroll_from_element(year,0,5).perform()
action.scroll_from_element(month,0,30).perform()
action.scroll_from_element(day,0,30).perform()
```



​		这里使用TouchActions类中的scroll_from_element()方法滑动元素：

+ on_eldment：滑动的元素
+ xoffset：x坐标距离
+ yoffset：y坐标距离

### 1.19 窗口截图

​		自动化测试用例是由程序执行的，因此有时候打印的错误信息不够直观。如果在脚本执行出错时能够对当前窗口进行截图并保存，那么通过截图就可以非常直观地看到脚本出错的原因。WebDriver提供了截图函数save_screenshot(),可用来截取当前窗口。

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
#截取当前窗口，指定截图图片的保存位置
driver.save_screenshot("./files/baidu_img.png")
```

​		WebDriver建议使用png作为图片的后缀名。脚本运行完成后，会在当前files/目录中生成baidu_img.png图片。

### 1.20 关闭窗口

​		在前面的例子中一直使用quit()方法，其含义为退出相关的驱动程序和关闭当前所有窗口。除此之外，WebDriver还提供了close()方法，用来关闭当前窗口。