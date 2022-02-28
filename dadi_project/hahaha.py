import os
import threading
import multiprocessing
#启动 redis
redis = r'E: && cd E:\Redis-x64-3.0.504 && redis-server.exe redis.windows.conf'
#启动 Mongo_DB
Mongo_DB = r'E: && cd E:\MongoDB\bin && mongod --dbpath E:\MongoDB\data\db'
#启动 easy-mock
easy_mock = r'E: && cd E:\Pythonprojects\easy-mock && npm run dev'

def start_redis(mas):
    os.system(redis)
def start_Mongo_DB(mas):
    os.system(Mongo_DB)
def start_easy_mock(mas):
    os.system(easy_mock)
if __name__ == '__main__':
    # 这里开启了4个进程
    pool = multiprocessing.Pool(processes=3)
    msg = "hello"
    pool.apply_async(start_redis, (msg,))
    pool.apply_async(start_Mongo_DB, (msg,))
    pool.apply_async(start_easy_mock, (msg,))


    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束


