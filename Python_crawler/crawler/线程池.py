import requests
import time
from multiprocessing.dummy import Pool
from lxml import etree
urls = [
    'http://127.0.0.1:5000/hyzhyz',
    'http://127.0.0.1:5000/llgllg'
]
def get_requests(url):
    page_text = requests.get(url).text
    return page_text

def parse(result):
    tree = etree.HTML(result)
    return tree


# #同步代码
# if __name__ == '__main__':
#     start = time.time()
#
#     for url in urls:
#         res = get_requests(url)
#         print(res)
#     print(f"总耗时：{time.time()-start}")


#异步代码
if __name__ == '__main__':
    start = time.time()
    pool = Pool(2)    #3表示开启线程的数量
    #使用get request作为回调函数，需要基于异步的形式对urls列表的每一个列表元素进行操作
    #保证回调函数必须要有一个参数和返回值
    #多个map并行同步
    result_list = pool.map(get_requests,urls)
    result_tree = pool.map(parse,result_list)
    # print(result_list)
    print(f'总耗时：{time.time()-start}')
