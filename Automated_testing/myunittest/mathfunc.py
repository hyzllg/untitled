import requests


def phone_01():
    url = 'http://apis.juhe.cn/mobile/get'
    params = {
        "key": "587a63506ac7c9ea98f3946631f3abfb",
        "phone": "16621381003"
    }
    res = requests.get(url, params=params)
    result = res.json()
    return result

def phone_02():
    url = 'http://apis.juhe.cn/mobile/get'
    params = {
        "key": "587a63506ac7c9ea98f3946631f3abfc",
        "phone": "16621381003"
    }
    res = requests.get(url, params=params)
    result = res.json()
    return result
