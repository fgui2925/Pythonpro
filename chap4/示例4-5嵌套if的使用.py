answer=input('前方是否有酒驾检查？')
if answer=='Y':
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('不构成酒驾，请通行。')
    elif proof<80:
        print('已构成酒驾，请不要开车！')
    else:
        print('已构成醉驾，请千万不要开车！')
else:
    print('无检查，请通行。')