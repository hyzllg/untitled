from aip import AipContentCensor
import requests

def get_apicontentcensor_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    grant_type = 'client_credentials'
    APP_ID = '24820996'
    client_id = 'LWKrUcRsztPuaerCk56f5ndU'
    client_secret = 'rEi9812yzgtXZqHQh2MNFbpbOaNDVcbH'
    data = {
        "grant_type" : grant_type,
        "client_id" : client_id,
        "client_secret" : client_secret
    }
    requit = requests.post(url,data=data)
    return requit.json()['access_token']
