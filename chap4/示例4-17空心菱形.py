'''
空心菱形，只需要在菱形中打印*的时候做一个判断，只打印每行的第一列和最后一列
'''

x = eval(input('请输入菱形的行数：'))     #这是老师的方法
while x%2==0:
    x=eval(input('输入的值不符合要求，请输入一个奇数行：'))
else:
    #上半部分
    top_row=x//2+1
    for i in range(1,top_row+1):   #上半部分的行数
        for j in range(1,top_row-i+1): #倒三角的列数
            print(' ',end='')
        for k in range(1,i*2-1+1): #等腰三角形的列数
            if k==1 or k==i*2-1:    #只在每行的第一列和最后一列打印*
                print('*',end='')
            else:
                print(' ',end='')
        print()
    #下半部分
    bottom_row=x//2
    for i in range(1,bottom_row+1):   #下半部分的行数
        for j in range(1,i+1):  #直角三角形的列数
            print(' ',end='')
        for k in range(1,x-i*2+1):   #倒等腰三角形的列数
            if k==1 or k==x-i*2:     #只在每行的第一列和最后一列打印*
                print('*',end='')
            else:
                print(' ',end='')
        print()


x = eval(input('请输入菱形的行数：'))           # 这是自己研究的方法
while x%2==0:
    x=eval(input('输入的值不符合要求，请输入一个奇数行：'))
else:
    for i in range(1,x+1):
        if i <= x//2+1:
            for j in range(1,x+1):
                #只在每行的第一列和最后一列打印*
                if j==(x//2+1)-i+1 or j==(((x//2+1)-i+1)+(i*2-1)-1):  #从(x//2-i)开始循环，循环i*2-1次，因为第一个点也算一次循环，所以循环次数需要减1
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
        else:
            for j in range(1,x+1):
                #只在每行的第一列和最后一列打印*
                if j==i-x//2 or j==((i-x//2)+((x+1-i)*2-1)-1):  #从i-x//2开始循环，循环（x+1-i）*2-1次，因为第一个点也算一次循环，所以循环次数需要减1
                    print('*',end='')
                else:
                    print(' ',end='')
            print()