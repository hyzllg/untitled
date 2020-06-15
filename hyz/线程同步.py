import threading
import random
import time

lock = threading.Lock()

list1 = [0] * 10

def task1():
    #获取线程锁，如果已经上锁，则等待锁的释放
    lock.acquire() #阻塞
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release()


def task2():
    lock.acquire()  # 阻塞
    for i in range(len(list1)):
        print('----->',i)
        time.sleep(0.5)
    lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()
