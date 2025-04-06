# 使用[]创建列表
lst=['hello','world',98,100.5]
print(lst)

# 可以使用内置的函数list()创建列表
lst1=list(('hello','world',98,100.5))
print(lst1)
lst2=list('helloworld')
print(lst2)
lst3=list(range(1,10,2)) #从1开始到10结束，步长为2，不包含10
print(lst3)

#列表是序列中的一种，对序列的操作符，运算符，函数均可以使用
print(lst+lst2+lst3)
print(lst*3)
print(len(lst))
#print(max(lst)) # TypeError: '>' not supported between instances of 'int' and 'str'
#print(min(lst)) # TypeError: '>' not supported between instances of 'int' and 'str'
print(max(lst3))
print(min(lst3))
print(lst.count(98)) #统计列表中红98出现的次数
print(lst.index(98)) #索引列表中98第一次出现的位置

#列表的删除操作
lst4=[10,20,30]
# del lst4[]  #删除整个列表
# print(lst4) #SyntaxError: invalid syntax