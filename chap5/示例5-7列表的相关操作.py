import copy

lst=['hello','world','python']
print('原列表：',lst,id(lst))

# 增加元素的操作
lst.append('php')
print('增加元素后：',lst,id(lst)) #元素个数可变，但是内存地址不变，所以列表是python中的可变数据类型

# 插入元素的操作
lst.insert(1,100)
print('插入元素后：',lst,id(lst))

# 列表元素的删除操作
lst.remove('python')
print('删除元素后：',lst,id(lst))

# 使用pop(index)根据索引将元素取出，然后再删除
print(lst.pop(1))
print(lst)

#清除列表中所有的元素clear()
# lst.clear()
# print('清除列表所有元素后：',lst,id(lst))
# 选中多条代码条目后，按ctrl+?，可以批量注释掉多行代码

# 列表的逆向输出
lst.reverse()
print('逆向输出后：',lst,id(lst))

# 列表的拷贝，将产生一个新的列表对象
new_lst=lst.copy()
print('原列表：',lst,id(lst))
print('拷贝后的新列表：',new_lst,id(new_lst))

# 列表的赋值，赋值后的列表与原列表指向的是同一块内存空间！！所有的可变数据类型的赋值都是一样的，指向的是同一块内存空间
new_lst2=lst
print('原列表：',lst,id(lst))
print('赋值后的列表：',new_lst2,id(new_lst2))

# 列表元素的修改操作
# 根据索引进行修改元素
lst[1]='mysql'
print('修改后的列表：',lst,id(lst))