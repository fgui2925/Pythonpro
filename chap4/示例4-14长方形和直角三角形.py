# 三行四列长方形
'''
****
****
****
'''
for i in range(1,4):
    for j in range(1,5): #内层循环
        print('*',end='')
    print() #空的print语句，作用是换行

print('------------')

# 五行五列直角三角形
'''
*
**
***
****
*****
'''
# 第一行1颗星，即内层循环1次；第二行2颗星，即内层循环2次；……第5行5颗星，即内层循环5次。
# 内层循环次数，跟行数相关。说明内层循环次数=行数。因为range()函数不含上限，上限需要加1。

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()

print('------------')

for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print('*',end='')
    print()
