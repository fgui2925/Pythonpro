try:
    x=int(input('请输入分数:'))
    if x<0 or x>100:
        print('分数不正确')
    elif 100 >= x >= 0:
        print('分数为:',x)
    else:
        raise Exception('invalid literal for int() with base 10',x)
except Exception as e:
    print(e)

try:
    x=int(input('请输入分数:'))
    if 0<= x <=100:
        print('分数为:',x)
    else:
        raise Exception('分数不正确')
except Exception as e:
    print(e)
