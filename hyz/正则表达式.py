import re
import requests
t = '<img id=" onlond="aleh&& alog" paiwjepawj" src="https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583400357&di=c131a505c36e4d939d14aaf77c448288&src=http://hbimg.b0.upaiyun.com/186c8a3359279f209791ce1c22a40834700cffd3990b-70uiaP_fw658"'
requst = re.match(r'.+ src="(.*?)"',t)
#去除图片网址
print(requst.group(1))
image_path = requst.group(1)

response = requests.get(image_path)

with open('aa.jpg','wb') as wstream:
    wstream.write(response.content)