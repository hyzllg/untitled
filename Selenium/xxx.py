import requests
import re
import time

s = requests.session()
def name_idno():
    url = f'http://www.xiaogongju.org/index.php/index/id.html/id/513224/year/1990/month/{time.strftime("%m")}/day/{time.strftime("%d")}/sex/%E7%94%B7'

    headers = {
        "Content-Type":"text/html;charset=utf-8",
        "Host":"www.xiaogongju.org",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    print("*********爬取姓名身份证信息*********")
    print(url)
    request = s.get(url,headers=headers)
    ret = request.text
    ret = re.findall('\s<td>\w*</td>',ret)
    new_ret = []
    for i in ret:
        i = i.replace(' ','')
        i = i.replace('<td>','')
        i = i.replace('</td>','')
        new_ret.append(i)
    print(new_ret)
    return new_ret

name_idno()