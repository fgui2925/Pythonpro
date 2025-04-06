# break语句的作用：当本次判断结果为True时，则跳出当前循环体。

s=0
i=1  # （1）初始化变量
while i<=10: #（2）判断条件
    #(3)语句块
    s+=i
    if s>20:
        print('累加和大于20的当前数是：',i)
        break
    i+=1  #(4)改变变量
print(s)

print('------------------')
#模拟用户登录
i=0   # （1）初始化变量
while i<3: #（2）判断条件
    #(3)语句块
    user_name=input('请输入用户名：')
    password=input('请输入密码：')
    if user_name=='admin' and password==('88888888'):
        print('登陆成功！')
        break
    else:
        if i<2:
            print('用户名或密码错误，您还有',2-i,'次登录机会')
    i+=1  #(4)改变变量
else:  #while...else
    print('3次输入错误，登录失败！请联系管理员')

