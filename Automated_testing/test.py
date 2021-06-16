from multiprocessing.dummy import Pool
import WZ_360
import WZ_HUANBEI
import WZ_PPDAI
import WZ_ORANGE


if __name__ == '__main__':
    #建立线程数
    pool = Pool(40)
    #走数据的笔数
    a = range(10)
    def Func_360(a):
        WZ_360.main(0, 1)
    def Func_HUANBEI(a):
        WZ_HUANBEI.main(0, 1)
    def Func_PPDAI(a):
        WZ_PPDAI.main(0, 1)
    def Func_ORANGE(a):
        WZ_ORANGE.main(0, 1)

    pool.map(Func_360,a)
    pool.map(Func_HUANBEI,a)
    # pool.map(Func_PPDAI,a)
    pool.map(Func_ORANGE,a)