import requests

class HttpClient:
    def __init__(self):
        self.session = requests.session()

    #封装请求 get post delete put ......
    #接口地址 url
    #接口参数 dada
    #参数类型 表单 json
    #请求头 数据雷士设置 **kwargs
    def send_request(self, method, url, param_type, data, **kwargs):
        #将请求方式转换成大写统一
        global response
        method = method.upper()
        #参数类型转换成大写统一
        param_type = param_type.upper()
        #判断请求方式
        if method == "GET":
            response = self.session.request(method=method, url=url, params=data, **kwargs)
        elif method == "POST":
            #判断请求参数类型
            if param_type == "FROM":
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif method == "DELETE":
            #判断请求参数类型
            if param_type == "FROM":
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif method == "PUT":
            #判断请求参数类型
            if param_type == "FROM":
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        else:
            print("检查参数！")
        return response

    def close_session(self):
        self.session.close()
