# def func():
#     i = 0
#     while i < 5:
#         # print(n)
#         temp = yield i
#         print('temp:',temp)
#         for i in range(temp):
#             print('------->')
#
#
#         i+=1
#     return '没有更多数据了'
#
#
#
# # yield n   #return n + 暂停
# # 得到生成器
# # 调用生成函数
# g = func()
# print(g.send(None))
# n1 =g.send(2)
# print('n1:',n1)



class Phone:
    def __init__(self):
        self.a = 'a'
        self.b= 'b'

    def cat(self):

        print('正在打电话！')


c = Phone()
print(c.a)
c.cat()