import requests

keyword = input("enter a key word:")
params = {
	'query':keyword
}
url = 'https://www.sogou.com/web'

requit = requests.get(url)
requit.encoding = 'utf-8'
with open('./')

print(requit.text)
