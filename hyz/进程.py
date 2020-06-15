import os
import time
from multiprocessing import Process
from multiprocessing import Pool
from random import random

def task(task_name):
        print('开始做任务了！',task_name)
        start = time.time()
        time.sleep(random()*2)
        end = time.time()
        return '完成任务用时!:',(end - start)

container = []
def callback_func(n):
    container.append(n)

if __name__ == '__main__':

    pool = Pool(5)
    tasks = ['听音乐','吃饭','洗衣服','打游戏','散步','笑','哭']
    for task1 in tasks:
        pool.apply_async(task,args=(task1,),callback=callback_func)



    pool.close()
    pool.join()
    for c in container:
        print(c)

    print('over!!!!!!')
