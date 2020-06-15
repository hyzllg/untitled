
# 小花猫
class Cat(object):
    type = '猫'
    type_en = 'cat'

    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    def eat(self, food):
        print('{}喜欢吃{}'.format(self.nickname, food))

    def catch_mouse(self, weight, color):
        print('{} 抓了一只{}kg的{}老鼠！'.format(self.nickname, weight, color))

    def sleep(self, hour):
        if hour < 5:
            print('需要睡觉！')
        else:
            print('可以工作！')

    def show_info(self):
        print('正在打印 详细信息')
        print(self.nickname, self.age, self.color)


cat_1 = Cat('花花', 2, '灰色')

cat_1.catch_mouse(0.5, '黑色')
cat_1.sleep(8)
cat_1.eat('小鱼干')

