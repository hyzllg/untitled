import requests
import sys

def response():
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
        print("cookies:%s" % (requit.cookies))
        print("headers:%s" % (requit.headers))
        print("url:%s" % (requit.url))


    except:
        print("获取token错误！")
        sys.exit()
    return requit.json()['access_token']

response()