s=0
for i in range(1,101):
    if i%2==1: #奇数
        continue #奇数时不再执行后面的代码了
    s+=i
print('1-100之间的偶数和为：',s)