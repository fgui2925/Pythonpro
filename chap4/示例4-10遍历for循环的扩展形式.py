#for循环正常执行完毕，执行else部分

s=0
for i in range(1,11):
    s+=i
else:
    print('1~10的累加和是：',s)