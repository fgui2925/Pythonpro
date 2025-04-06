d={1001:'张三',1002:'李四',1003:'王五'}
print(d)

# 向字典中添加元素
d[1004]='赵六'  #直接赋值
print(d)

# 获取字典中所有的key
keys=d.keys()
print(keys) # 得到的是一个对象dict_keys([1001, 1002, 1003, 1004])
print(list(keys))
print(tuple(keys))

# 获取字典中所有的value
values=d.values()
print(values)  #得到的是一个对象dict_values(['张三', '李四', '王五', '赵六'])
print(list(values))
print(tuple(values))

# 将字典中的数据转成key-value的形式,以列表的方式进行展示
lst=tuple(d.items())  #d.items():获取字典中的键值对，并输出为元组类型
print(lst,type(lst))

d=dict(lst)
print(d,type(d))

# 使用pop函数进行删除
print(d.pop(1001)) #先取出要删除的key-value
print(d) #再对字典进行输出

print(d.pop(1008,'不存在'))

# 随机删除
print(d.popitem()) #先取出要删除的key-value
print(d) #再对字典进行输出

# 清空字典中的所有元素
d.clear()
print(d)
# python中一切皆对象，每个对象都有一个布尔值
print(bool(d))