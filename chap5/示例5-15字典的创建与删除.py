# （1）创建字典
d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d) # key相同时,value进行了覆盖

# （2）zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
d=zip(lst1,lst2)
print(d)  # zip()函数生成的结果是一个zip对象，如果想看到结果，需要转成字典类型
#print(list(d)) #[(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]
d=dict(d) #使用dict()函数，将结果转成字典类型
print(d)

# (3)使用参数创建字典
d=dict(cat=10,dog=20) #左侧cat是key,右侧是value
print(d)

t=(10,20,30)
print({t:10}) #元组是可以作为字典中的key

# lst=[10,20,30]
# print({lst:10}) #TypeError: unhashable type: 'list'
# 列表是可变数据类型，不可以作为字典中的key

# 字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))

# 字典的删除
del d
# print(d) # NameError: name 'd' is not defined
