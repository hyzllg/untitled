import pytest
from selenium import webdriver

# @pytest.fixture()
# def fixture():
#     return 666

@pytest.fixture()
def driver_fixture():
    print("创建浏览器对象")
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    driver.maximize_window()
    # 隐式等待 等待页面元素全部加载
    driver.implicitly_wait(10)
    return driver