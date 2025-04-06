try:
    x1 = int(input('请输入第一条边:'))
    x2 = int(input('请输入第二条边:'))
    x3 = int(input('请输入第三条边:'))
    if x1+x2>x3 and x1+x3>x2 and x2+x3>x1:
        print('三角形的边长为:a={0},b={1},c={2}'.format(x1,x2,x3))
    else:
        raise Exception('a={0},b={1},c={2}不能构成三角形'.format(x1,x2,x3))
except Exception as e:
    print(e)

