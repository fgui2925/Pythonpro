# 遍历字符串
for i in 'hello':
    print(i)

#range()函数，python中的内置函数，产生一个[n,m)的整数序列，包含n,不含m
for i in range(1,11):
    print(i)
    if i%2==0:
        print(i,'是偶数')

# 计算1-10之间的累加和
s=0
for i in range(1,11):
    s+=i
print('1~10的累加和是：',s)

#输出100-999之间的水仙花数
print('----100-999之间的水仙花数有：-----')
for i in range(100,1000):
    a=i%10 #获取个位上的数
    b=i//10%10 #获取十位上的数
    c=i//100%10 #获取百位上的数
    if a**3+b**3+c**3==i:
        print(i)