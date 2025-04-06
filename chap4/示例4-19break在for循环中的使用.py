for i in 'hello':
    if i=='e':
        break
    print(i)

print('----------')

for i in range(3):
    user_name = input('请输入用户名：')
    password = input('请输入密码：')
    if user_name == 'admin' and password == ('88888888'):
        print('登陆成功！')
        break
    else:
        if i < 2:
            print('用户名或密码错误，您还有', 2 - i, '次登录机会')
else:  # for...else
    print('3次输入错误，登录失败！请联系管理员')