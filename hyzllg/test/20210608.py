import requests
from lxml import etree


headers = {
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}

'''

'''
# #封装一个代理池
# url = ''
# page_text = requests.get(url,headers=headers).text
# tree = etree.HTML(page_text)
# proxy_list = tree.xpath()
# http_proxy = []#代理池
# for proxy in proxy_list:
# 	dic = {
# 		'http':proxy
# 	}
# 	http_proxy.append(dic)
# http_proxy


#url模板
url = 'https://www.kuaidaili.com/free/intr/%d/'
ips = []
for page in range(1,100):
	new_url = format(url%page)
	#让当次的请求使用代理机制，就可以更换请求的ip地址
	# page_text = requests.get(url=new_url,headers=headers,proxies={'http':ip:port}).text
	page_text = requests.get(url=new_url,headers=headers).text

	tree = etree.HTML(page_text)
	#在xpath表达式中不可以出现tbody标签
	tr_list = tree.xpath('//*[@id="list"]/table//tr')
	for tr in tr_list:
		ip = tr.xpath('./td[1]/text()')[0]
		port = tr.xpath('./td[2]/text()')[0]
		print(ip,port)
		ips.append(ip)
print(len(ips))