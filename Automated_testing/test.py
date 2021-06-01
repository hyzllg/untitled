import requests

url = 'https://www.baidu.com/'

requit = requests.get(url)
requit.encoding = 'utf-8'

print(requit.text)
