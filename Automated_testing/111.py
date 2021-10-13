def start_lj_mock():
    import requests
    url = "http://10.1.14.191:26275/sys/setMockStatus?fundCode=20062&status=1"
    response = requests.request("GET", url)
    print("龙江放款mock开启成功！")

start_lj_mock()