# 五行五列倒三角形
'''
*****
****
***
**
*
'''
# 第一行5颗星，即内层循环5次；第二行4颗星，即内层循环4次；……第5行1颗星，即内层循环1次。
# 内层循环次数，跟行数相关。说明内层循环次数+行数=6，即内层循环次数=6-行数。因为range()函数不含上限，上限需要加1。

for i in range(1, 6):           #这是老师教学的方法
    for j in range(1, 7-i):
        print('*', end='')
    print()

print('------------')

for i in range(1,6):
    for j in range(1,6):          #这是自己研究的方法
        if j<=6-i:
            print('*',end='')
    print()

print('------------')


# 五行九列等腰三角形
'''
&&&&*
&&&***
&&*****
&*******
*********
'''
# 需要先打印一个倒三角，再打印等腰三角形，所以内部有两个循环。
# 倒三角的写法上面已经介绍过了。
# 等腰三角形：第一行1颗星，即内层循环1次；第二行3颗星，即内层循环3次；……第5行9颗星，即内层循环9次。
# 内层循环次数，跟行数相关，即内层循环次数=行数*2-1。因为range()函数不含上限，上限需要加1。

for i in range(1,6):          #这是老师教学的方法
    for j in range(1, 7-i):
        print(' ', end='')
    for k in range(1, i*2):
        print('*', end='')
    print()


print('------------')
'''
    *
   ***
  *****
 *******
*********
'''
# 第一行1颗星，即内层循环1次，从第5列开始；第二行3颗星，即内层循环3次，从第4列开始；……第5行9颗星，即内层循环9次，从第1列开始。
# 内层循环次数，跟行数相关，即内层循环次数=行数*2-1。内层循环开始点，也跟行数相关，即内层循环开始点=6-行数。因为range()函数不含上限，上限需要加1。

for i in range(1,6):          #这是自己研究的方法
    for j in range(1,10):
        if j>=(6-i) and j<=(6-i)+(2*i-1)-1:  #从6-i列开始，循环次数为2*i-1，因为第一列也算一次循环，所以循环次数还需要再减去1
            print('*',end='')
        else:
            print(' ',end='')
    print()

print('------------')