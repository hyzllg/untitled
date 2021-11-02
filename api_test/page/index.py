from selenium.webdriver.common.by import By
from test_selenium.page.login import Login
import requests
import pytest

class Index:

    def index(self,token,text):
        url = 'https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined'
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "text": text
        }
        access_token = token
        request_url = url + "?access_token=" + access_token
        requit = requests.post(request_url,data=data,headers=headers)
        page = requit.json()['conclusion']
        return page

