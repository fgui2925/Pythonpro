# 使用()创建元组
t=('hello','world',98,100.5)
print(t)

# 可以使用内置的函数tuple()创建元组
t1=tuple(['hello','world',98,100.5])
print(t1)
t2=tuple('helloworld')
print(t2)
t3=tuple(range(1,10,2)) #从1开始到10结束，步长为2，不包含10
print(t3)
t4=tuple([10,20,30,40])
print(t4)

#元组是序列中的一种，对序列的操作符，运算符，函数均可以使用
print(t+t2+t3)
print(t*3)
print(10 not in t)
print(len(t))
# print(max(t)) # TypeError: '>' not supported between instances of 'int' and 'str'
# print(min(t)) # TypeError: '>' not supported between instances of 'int' and 'str'
print(max(t3))
print(min(t3))
print(t.count(98)) #统计列表中红98出现的次数
print(t.index(98)) #索引列表中98第一次出现的位置

# 如果元组中只有一个元素，逗号不能省
t=(10)
print(t,type(t))  #<class 'int'>
t=(10,)
print(t,type(t))  #<class 'tuple'>

#元组的删除操作
t5=(10,20,30)
del t5
#print(t5) # NameError: name 't5' is not defined
#del t5[0] # TypeError: 'tuple' object doesn't support item deletion