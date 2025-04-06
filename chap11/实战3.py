import time

def login(name,pwd):
    if name=='admin' and pwd=='admin':
        with open('登录日志.txt','a',encoding='utf-8') as f:
            f.write('用户名:'+name)
            f.write('登录时间:'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            f.write('\n')
        print('登陆成功！')
        return True
    else:
        print('用户名或密码不正确')
        return False

def show_massage(s):
    while s:
        num=input('输入提示数字,执行相应操作:0,退出 1,查看登录日志\n请输入您要操作的数字:')
        if num=='1':
            with open('登录日志.txt','r',encoding='utf-8') as f:
                for item in f.readlines():
                    print(item)
        elif num=='0':
            print('退出成功')
            break
        else:
            pass

if __name__ == '__main__':
    user_name=input('请输入用户名:')
    password=input('请输入密码:')
    result=login(user_name,password)
    show_massage(result)