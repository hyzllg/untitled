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

from selenium.webdriver.common.keys import keys

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

![](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593859669253.png)

​	本例中，通过as关键字将expected_conditions重命名为EC，并调用presence_of_element_located()方法判断元素是否存在

![](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593859610301.png)

​	除expected——conditions类提供的丰富的预期条件判断方法外，还可以利用前面学到的is_displayed()方法自己实现元素显式等待。

​	![](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593859898913.png)

​	相对来说，这种方式更容易理解。首先for循环10次，然后通过is_displayed()方法循环判断元素是否可见。如果为True，则说明元素可见，执行break跳出循环；否则执行sleep()休眠1s继续循环判断。10次循环结束后，如果没有执行break，则执行for循环对应的else语句，打印“time out”信息。

#### 1.7.2 隐式等待

WebDriver提供了implicitly_wait()方法可以用来实现隐式等地，用方法来说要简单的多。

![](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593860199473.png)

![](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593860216903.png)

​	implicitly_wait()的参数是时间，单位为秒，本例中设置的等待时间是10s。首先，这10s并非一个固定的等待时间，它并不影响脚本的执行速度。其次，它会等待页面上的所有元素。当脚本执行到某个元素定位时，如果元素存在，则继续运行；如果定位不到元素，则它将进行轮询的方式不断地判断元素是否存在。假设在第6s定位到了元素，则继续运行，若直到超出设置时间还没有定位到元素，则抛出异常。

### 1.8 定位一组元素

WebDriver还提供了8种用于定位一组元素的方法：

![](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593864795483.png)

定位一组元素的方法与定位单个元素的方法非常像，唯一的区别是单词“element”后面多了个“s”，用来表示复数。

![1593864874490](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593864874490.png)

![1593864888778](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593864888778.png)

运行结果：

![1593864909907](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593864909907.png)

### 1.9 多表单切换

​		在Web应用中经常会遇到frame/iframe表单嵌套页面的应用，WebDriver只能在一个页面上对元素进行识别和定位，无法直接定位frame/iframe表单内嵌页面上的元素，这时就需要通过swich_to.frame()方法将当前定位的主体切换为frame/iframe表单的内嵌页面。

![1593865182586](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593865182586.png)

​		switch_to.frame()默认可以直接对表单的id属性或name属性传参，因而可以定位元素的对象。在这个例子中，表单的id属性后半部分的数字（1553484417298.5217）是随机变化的，在CSS定位方法中，可以通过“^=“匹配id属性为以”x-URS-iframe"开头的元素。

​		最后，通过swith_to.default_content()回到最外层的页面。

### 1.10 多窗口切换

​		在页面操作过程中，有时单击某个链接会弹出新的窗口，这时就需要切换到新打开的窗口中进行操作。WevDriver提供的switch_to.window()方法可以实现在不同的窗口间切换。

+ current_window_handle:获得当前窗口句柄

+ window_handles:返回所有窗口的句柄到当前会话

+ switch_to.window():切换到相应的窗口

  ​	以百度首页和账号注册页为例，在两个窗口之间的切换

![1593865615313](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593865615313.png)![1593865625052](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593865625052.png)

​		脚本的执行过程：首先打开百度首页，通过current_window_handle获得当前窗口句柄，并赋值给变量search_handle。接着打开登陆窗口，在登录弹窗上单击“立即注册”链接，从而打开新的注册窗口。通过window_handles获得当前所有窗口句柄（包含百度首页和账号注册页），并赋值给变量all_handles。

​		循环遍历all_handles，如果handle不等于search_handles,那么一定是注册窗口，因为在脚本执行过程中只打开了两个窗口。然后，通过switch_to.window()切换到账号注册页。

### 1.11 警告框处理

​		在WebDriver中处理JavaScript生成的alert、confirm和prompt十分简单，具体做法是，首先使用switch_to.alert()方法定位，然后使用text、accept、dismiss、send_keys等进行操作。

+ text：返回alert、confirm、prompt中的文字信息

+ accept（）：接受现有警告框

+ dismiss（）：解散现有警告框

+ send_keys()：在警告框中输入文本（如果可以输入的话）

  可以使用switch_to.alert()方法为百度搜索设置弹窗

![1593866257114](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593866257114.png)

​		这里以百度搜索设置为例，打开百度瞍索设置，设置完成后单击“保存设置”按钮，弹出保存确认警告框。通过switch_to.alert获取当前页面上的警告框，text用于获取警告框提示信息，accept()于接受警告框。

### 1.12 下拉框处理

​		下拉框是Web页面常见功能之一，WebDriver提供了Select类来处理下拉框：

+ Select类：用于定位<select>标签

+ select_by_value()：通过value值定位下拉选项

+ select_by_visible_text()：通过text值定位下拉选项

+ select_by_index()：根据下拉选项的索引进行选择。第一个选项为0，第二个选项为1

  以百度搜索设置为例，下拉框代码如下：

  ![1593867058541](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593867058541.png)

  通过WevDriver代码操作下拉框：

  ![1593867092932](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593867092932.png)

  ![1593867122898](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593867122898.png)

### 1.13 上传文件

​		上传文件是比较常见的Web功能之一，但WebDriver并没有提供专门用于上传的方法，实现文件上传的关键在于思路。

​		在Web页面中，文件上传操作一般需要单击"上传"按钮后打开本地wndows窗囗，从窗囗中选择本地文件进行上传。因为WebDriver无法操作Wndows控件，所以对于初学者来说，一般思路会卡在如何识别wndows控件这个问题上。

​			在web页面中一般通过以下两种方式实现文件上传：

+ 普通上传：将本地文件路径作为一个值放在input标签中，通过form表单将这个值提交给服务器。

+ 插件上传：一般是指基于FIash、JavaScript或Ajax等技术实现的上传功能。

  ​	对于通过input标签实现的上传功能，可以将其看作一个输入框，即通过send_keys()指定本地文件路径的方式实现文件上传。

![1593867676439](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593867676439.png)

![1593867720672](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593867720672.png)

通过浏览器打开upfile.html文件，效果如图所示

![1593867765647](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593867765647.png)

![1593867776351](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593867776351.png)

​		这里测试的页面（upfile.html）和上传的文件（test.txt）位于与当前程序同目录的files/目录下

​		通过这种方式上传，就避免了操作Windows控件。如果能找到上传的input标签，那么基本可以通过send_keys()方法输入一个本地文件路径实现上传

​		对于插件上传，我们可以使用Autolt来实现

### 1.14 下载文件

​		Webdriver允许我们设置默认的文件下载路径，也就是说，文件会自动下载并且存放到设置的目录中，不同的浏览器设置方式不同。

​		下面以Firefox浏览器为例，演示文件的下载：

![1593868058374](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593868058374.png)

​		为了能在Firefox浏览器中实现文件的下载，我们需要通过FirefoxProfile()对其做一些设置。

![1593868122844](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593868122844.png)

​		设置为0，表示文件会下载到浏览器默认的下载路径；设置为2，表示文件会下载到指定的目录。

![1593868184860](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593868184860.png)

​		指定要下载文件的类型，即Content-type值，“binary/octet-stream”用于表示二进制文件。

​		HTTP Content-type 常用对照表参见http://tool.oschina.net/commons

​		可以通过在Firefox浏览器地址栏输入“about:config"进行参数的设置

​		在调用WebDriver的Firefox类时将所有设置选项作为firefox_profile参数传递给Firefox浏览器。Firefox浏览器在下载时会根据这些设置将文件下载到当前脚本目录下。



下面以Chrome浏览器为例，演示文件的下载。

![1593868476249](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593868476249.png)

Chrome浏览器在下载时默认不会弹出下载窗口，这里主要想修改默认的下载路径。

![1593868532830](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593868532830.png)

设置为0，表示禁止弹出下载窗口

![1593868579095](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593868579095.png)

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

  ![1593869550026](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593869550026.png)

  执行结果如下：

  ![1593869584666](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593869584666.png)

  ![1593869600377](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593869600377.png)

​        从执行结果可以看出，Cookie中的数据时以字典形式存放的。知道了Cookie中数据的存放形式后，即可按照这种形式向浏览器中添加Cookie

![1593870105754](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593870105754.png)

​		执行结果如下：![1593870132848](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593870132848.png)

​		从执行结果可以看出，最后一条Cookie是在脚本执行过程中通过add_cookie()方法添加的。通过遍历得到所有的Cookie，从而找到字典中key为”name“和”value”的Cookie值。

​		delete_cookie()和delete_all_cookies()方法的使用也很简单，前者通过name删除一个指定的Cookie，后者直接删除浏览器中的所有Cookies。

### 1.16 调用JavaScript

​		有些页面操作不能依靠WebDriver提供的API来实现，如浏览器滚动条的拖动。这时就需要借助JavaScript脚本。WevDriver提供了execute_script()方法来执行JavaScript代码。

​		用于调整浏览器滚动条位置的JavaScript代码如下：

![1593870497455](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593870497455.png)

​		window.scrollTp()方法用于设置浏览器窗口滚动条的水平位置和垂直位置。第一个参数表示水平的左边距，第二个参数表示垂直的上边距，代码如下：

![1593870588010](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593870588010.png)

​		首先，在浏览器中打开百度，搜索“selenium”，通过set_window_size()方法将浏览器窗口设置为固定宽、高显式，目的是让窗口出现水平和垂直滚动条。然后，通过execute_script()方法执行JavaScript代码来控制浏览器滚动条的位置。

​		当然，Javascript的作用不仅仅体现在浏览器滚动条的操作上，它还可以在页面中textarea文本框中输入内容。

![1593870806093](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593870806093.png)

​		文本框的HTML代码如下：

![1593870829744](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593870829744.png)

​		虽然可以通过id定位元素，但是不能通过send_keys()在文本框中输入文本信息。在这种情况下，可以借助JavaScript代码输入文本信息。

![1593870891483](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593870891483.png)

​		首先，定义要输入的内容text。然后，将text与JavaScript代码通过“+”进行拼接，这样做的目的是为了方便自定义输入内容。最后，通过execute_script()执行JavaScript代码。

### 1.17 处理HTML5视频播放

​		HTML5技术非常流行，主流的浏览器都支持HTML5，越来越多的应用使用HTML5的元素，如canvas、video等。另外，玩也存储功能提升了用户的网络体验，使得越来越多的开发者开始使用HTML5。

​		WebDriver支持在指定的浏览器上测试HTML5，另外，还可以使用JavaScript测试这些功能，这样就可以在任意浏览器上测试HTML5了。

​		大多数浏览器使用插件播放视频，但是，不同的浏览器需要使用不同的插件。HTML5定义了一个新的元素<video>，指定了一个标准的方式嵌入电影片段。HTML5 VIdeo Player，IE9+，Firefox，Opera,Chrome都支持元素<video>。

​		下面介绍如何自动化测试<video>,<video>提供了JavaScript接口和多种方法及属性。

![1593871388820](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593871388820.png)

​		JavaScript有个内置的对象叫作arguments。arguments包含了函数调用的参数数组，[0]表示取对象的第一个值。

​		currentSrc返回当前音频/视频的URL。如果未设置音频/视频，则返回空字符串。

​		load(),play()和pause()控制视频的加载，播放和暂停。

### 1.18 滑动解锁

​		滑动解锁如图：

![1593871602893](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593871602893.png)

​		当我们单击滑块时，改变的只是CSS样式，HTML代码段如下：
![1593871671602](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593871671602.png)

​		slide-to-unlock-handle表示滑块。在滑动过程中，滑块的左边距离会逐渐变大，因为它在向右移动。

​		slide-to-unlock-progress表示滑过之后的背景色，背景色的区域会逐渐增加，因为滑块在向右移动。

![1593871807690](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593871807690.png)

​		在这个脚本中，用到下面几个方法：

+ click_and_hold()：单击并按下鼠标左键，在鼠标事件中介绍过
+ move_by_offset()：移动鼠标，第一个参数为x坐标距离，第二个参数为y坐标距离
+ reset_action()：重置action

​       执行完成，滑动效果：

![1593871982101](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593871982101.png)

​		另一种应用，上下滑动选择日期：

![1593872021148](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593872021148.png)

​		参考前面的操作，通过ActionChains类可以实现上下滑动选择日期，但是这里要介绍另外一种方法，及通过TouchActions类实现上下滑动选择日期。

![1593872112058](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593872112058.png)

![1593872120534](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593872120534.png)

​		这里使用TouchActions类中的scroll_from_element()方法滑动元素：

+ on_eldment：滑动的元素
+ xoffset：x坐标距离
+ yoffset：y坐标距离

### 1.19 窗口截图

​		自动化测试用例是由程序执行的，因此有时候打印的错误信息不够直观。如果在脚本执行出错时能够对当前窗口进行截图并保存，那么通过截图就可以非常直观地看到脚本出错的原因。WebDriver提供了截图函数save_screenshot(),可用来截取当前窗口。

![1593872416646](C:\Users\16621\AppData\Roaming\Typora\typora-user-images\1593872416646.png)

​		WebDriver建议使用png作为图片的后缀名。脚本运行完成后，会在当前files/目录中生成baidu_img.png图片。

### 1.20 关闭窗口

​		在前面的例子中一直使用quit()方法，其含义为退出相关的驱动程序和关闭当前所有窗口。除此之外，WebDriver还提供了close()方法，用来关闭当前窗口。