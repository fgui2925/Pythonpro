t=(i for i in range(5))
print(t) #元组生成式生成的结果是一个生成器对象，如果想看到结果，需要转成元组类型
t=tuple (t)
print(t)

# 遍历
for item in t:
    print(item)

print('-'*40)

# 使用.__next__方法可以把元组生成式生成的结果按序取出来
t=(i for i in range(5))
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())

t=tuple (t) # 上述.__next__方法已经把元组的元素取完了
print(t)

