from aip import AipContentCensor
import requests
import sys

def get_apicontentcensor_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    grant_type = 'client_credentials'
    client_id = 'LWKrUcRsztPuaerCk56f5ndU'
    client_secret = 'rEi9812yzgtXZqHQh2MNFbpbOaNDVcbH'
    data = {
        "grant_type" : grant_type,
        "client_id" : client_id,
        "client_secret" : client_secret
    }
    #获取access_token
    try:
        requit = requests.post(url,data=data)

    except:
        print("获取token错误！")
        sys.exit()
    return requit.json()['access_token']


