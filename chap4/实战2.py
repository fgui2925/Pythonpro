#------使用if条件判断执行查询功能-----
print('''-------欢迎使用10086查询功能-----
1.查询当前余额
2.查询当前的剩余流量，单位为G
3.显示当前的剩余通话，单位为分钟
0.退出查询系统''')
answer='Y'
while answer=='Y':
    num = input('请输入您要执行的操作：')
    if num=='1':
        print('当前的余额为：100元')
        answer = input('还需要继续操作吗？Y或N')
    elif num=='2':
        print('当前的剩余流量为：50')
        answer = input('还需要继续操作吗？Y或N')
    elif num=='3':
        print('当前的剩余通话时间为：39分钟')
        answer = input('还需要继续操作吗？Y或N')
    elif num=='0':
        print('正在为您退出当前系统')
        break
    else:
        print('输入的指令不正确，请重新请输入!')
else:
    print('谢谢您的使用！')

#------使用match...case匹配判断执行查询功能-----
print('''-------欢迎使用10086查询功能-----
1.查询当前余额
2.查询当前的剩余流量，单位为G
3.显示当前的剩余通话，单位为分钟
0.退出查询系统''')
answer='Y'
while answer=='Y':
    num = input('请输入您要执行的操作：')
    match num:
        case '1':
            print('当前的余额为：100元')
            answer = input('还需要继续操作吗？Y或N')
        case '2':
            print('当前的剩余流量为：50')
            answer = input('还需要继续操作吗？Y或N')
        case '3':
            print('当前的剩余通话时间为：39分钟')
            answer = input('还需要继续操作吗？Y或N')
        case '0':
            print('正在为您退出当前系统')
            break
        case _:
            print('输入的指令不正确，请重新请输入!')
else:
    print('谢谢您的使用！')