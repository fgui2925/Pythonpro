s={10,20,30}

#向集合中添加元素
s.add(40)
print(s)
#删除元素
s.remove(40)
print(s)
#清空集合中的元素
# s.clear()
# print(s)

# 集合的遍历操作
for item in s:
    print(item)
# 使用enumerate()函数进行遍历
for index,item in enumerate(s,start=5): #index是序号，不是索引
    print(index,item)

# 集合的生成式
s={i for i in range(1,10)}
print(s)

s={i for i in range(1,10) if i%2==1}
print(s)

