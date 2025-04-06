import random
rand=random.randint(1,100) #产生1-100之间的随机数
i=1
while i<=10:
    num=eval(input('在我心中有个数，1-100之间，请你猜一猜：'))
    if num>rand:
        print('大了')
        i+=1
    elif num<rand:
        print('小了')
        i+=1
    else:
        print('猜对了')
        if i <= 3:
            print('真聪明，一共猜了', i, '次')
        elif 7 > i > 3:
            print('还可以，一共猜了', i, '次')
        else:
            print('猜的次数有点多啊，一共猜了', i, '次')
        break
else: # while...else..
    print('很抱歉10次机会已用完')