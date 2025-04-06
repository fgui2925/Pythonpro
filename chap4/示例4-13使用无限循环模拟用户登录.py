i=0  #（1）初始化变量
while i<3:  #（2）条件判断
    user_name = input('请输入用户名：')
    password = input('请输入密码：')
    if user_name=='admin' and password=='88888888':
        print('登录成功！')
        #需要改变循环变量，结束循环
        i=8  #(4)改变变量--用户名正确时
    else:
        if i<2:
            print('用户名或密码不正确，您还有',2-i,'次机会')
    i+=1   #(4)改变变量--用户名不正确时
#单分支的判断
if i==3:
    print('3次输入错误，登录失败！请联系管理员')