import requests
import json




def InsureInfo_request():
    headers = {
        'Content-Type': 'application/json'
    }
    url = 'http://10.1.14.106:27405/channel/apitest/QFIN/INSURE_INFO'
    data1 = {"channelCustId":"","name":"","insuranceNo":"2021092410102392532","idNo":"622924199112248835","idAddress":"上海市浦东新区龙阳路幸福村520号","phone":"16609242423","amount":6000,"periods":"6","purpose":"07","capitalCode":"FBBANK","custGrde":18,"email":"1264311721@hrtx.com","contactPhone":"18968523600","callbackUrl":"https://www.baidu.com"}
    response = requests.request("post",url,headers=headers,data=json.dumps(data1))
    result = response.json()
    return result

print(InsureInfo_request())