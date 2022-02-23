import requests
import yaml
import os


class Mock_Switch:
    # 多套环境，需传入对应ip端口
    '''
    10.1.14.191:26275 sit
    10.1.14.192:26275 uat
    10.1.14.191:20062 DEV
    '''
    def __init__(self,IP,Port):#两个参数，IP和端口
        self.IP = IP
        self.Port = Port

    #启用龙江放款mock
    def start_lj_mock(self):
        url = f"http://%s:%s/sys/setMockStatus?fundCode=20062&status=1" % (self.IP,self.Port)
        response = requests.request("GET", url)
        result = response.json()
        if (result['data']['status']) == '1':
            print("龙江放款mock开启成功！")
        else:
            print("龙江放款mock开启失败！")
    #关闭龙江放款mock
    def end_lj_mock(self):
        url = f"http://{self.IP}:{self.Port}/sys/setMockStatus?fundCode=20062&status=0"
        response = requests.request("GET", url)
        result = response.json()
        if (result['data']['status']) == '0':
            print("龙江放款mock关闭成功！")
        else:
            print("龙江放款mock关闭失败！")

    #启用交行放款mock
    def start_jh_mock(self):
        url = f"http://{self.IP}:{self.Port}/sys/setMockStatus?fundCode=301&status=1"
        response = requests.request("GET", url)
        result = response.json()
        if (result['data']['status']) == '1':
            print("交行放款mock开启成功！")
        else:
            print("交行放款mock开启失败！")
    def end_jh_mock(self):
        url = f"http://{self.IP}:{self.Port}/sys/setMockStatus?fundCode=301&status=0"
        response = requests.request("GET", url)
        result = response.json()
        if (result['data']['status']) == '0':
            print("交行放款mock关闭成功！")
        else:
            print("交行放款mock关闭失败！")
    #启用交行放款mock
    def start_fb_mock(self):
        url = f"http://{self.IP}:{self.Port}/sys/setMockStatus?fundCode=787&status=1"
        response = requests.request("GET", url)
        result = response.json()
        if (result['data']['status']) == '1':
            print("富邦放款mock开启成功！")
        else:
            print("富邦放款mock开启失败！")
    #关闭交行放款mock
    def end_fb_mock(self):
        url = f"http://{self.IP}:{self.Port}/sys/setMockStatus?fundCode=787&status=0"
        response = requests.request("GET", url)
        result = response.json()
        if (result['data']['status']) == '0':
            print("富邦放款mock关闭成功！")
        else:
            print("富邦放款mock关闭失败！")