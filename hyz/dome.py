import json
a = {
                "agentNo":"TianCheng",
                "agentName":"甜橙保代",
                "loanReqNo":"2020070152013140001",
                "insReqNo":"",
                "name":"哑巴湖大水怪",
                "idNo":"412721198705203577",
                "phone":"16613145219",
                "amount": 5000,
                "periods":3,
                "purpose":"01",
                "premiumRate":0.08,
                "insurantName":"哑巴湖大水怪",
                "insurantAdd":"被保险人通讯地址",
                "postCode":"110016",
                "stage":"01"
            }
print(type(a))
a = json.dumps(a)
print(type(a))

