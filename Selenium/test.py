import random
for j in range(1,4):
    word = input('请输入账号')
    password = input('请输入密码')
    a = 'zhangningyu'
    b = '123456'
    c = '0123456789qwertyuiopshgmfcvnmkDFBNMGTRUIYEQSCGG'
    code_ = ''
    for i in range(4):
        k = c[random.randint(0, len(c)-1)]
        code_ += k
    print(code_)
    code = input('请输入验证码')
    if word == a and password == b and code == code_:
        print('登录成功')
        break
    else:
        print('登录失败,你还剩{}次机会'.format(3-j))
else:
    print('三次机会已使用完毕')