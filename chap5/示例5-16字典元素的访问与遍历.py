d={'python':10,'hello':20,'world':30}

# (1)使用d[key]获取key对应的数据
print(d['python'])
# （2）使用d.get(key)方法获取key对应的数据
print(d.get('python'))

# 二者之间是有区别的，如果key不存在，d[key]报错，d.get(key)可以指定默认值
# print(d['Java']) # KeyError: 'Java'
print(d.get('Java'))  #None
print(d.get('Java','不存在')) #指定默认值=不存在

# 字典的遍历。用d.items()
for item in d.items():
    print(item) #得到key-value键值对（元组类型）

# 使用for循环时，分别获取key,value
for key,value in d.items():
    print(key,value)