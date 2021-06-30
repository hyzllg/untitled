from multiprocessing.dummy import Pool
import WZ_360
import WZ_HUANBEI
import WZ_PPDAI
import WZ_ORANGE
from time import time
from time import sleep

a = range(5)
# 测试环境选择
test = 0
# 走数据的笔数
number = 3

# def WZ_360_(a):
#     WZ_360.main(test, number)
# def WZ_HUANBEI_(a):
#     WZ_HUANBEI.main(test, number)
# def WZ_PPDAI_(a):
#     WZ_PPDAI.main(test, number)
# def WZ_ORANGE_(a):
#     WZ_ORANGE.main(test, number)

def batch(a):
    WZ_360.main(test, number)
    WZ_HUANBEI.main(test, number)
    WZ_PPDAI.main(test, number)
    WZ_ORANGE.main(test, number)


if __name__ == '__main__':
    start = time()
    #建立线程数
    # pool = Pool(10)
    # pool.map(batch,a)
    batch(a)
    end = time()
    print(f"消耗时间：{end-start}")

