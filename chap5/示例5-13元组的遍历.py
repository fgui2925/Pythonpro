t=('hello','world','python','php')

#使用for循环进行遍历
for i in t:
    print(i)

#使用for range() len()进行索引查询遍历
for i in range(len(t)):
    print(i,t[i])

#使用emulate()进行遍历：
for index,item in enumerate(t): #index是序号，不是索引
    print(index,item)

# 修改序号
for index,item in enumerate(t,start=5):
    print(index,item)