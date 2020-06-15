import random
class Road:
    def __init__(self,name,len):
        self.name = name
        self.len = len
    print('---------')

class Cat:
    def __init__(self,brand,speed):
        self.__brand = brand
        self.__speed = speed
    @property
    def get(self):
        return self.__brand
    @get.setter
    def get(self,brand):
        self.__brand = brand

    def ran(self,road):
        ran_time = random.randint(1,10)
        print('{}在{}以{}的速度行驶了{}小时'.format(self.__brand,road.name,self.__speed,ran_time))

    def __str__(self):
        return '车型{}，速度{}'.format(self.__brand,self.__speed)
r = Road('京哈高速',120000)
c = Cat('悍马',120)
c.ran(r)
c.get = '大奔'
print(c)