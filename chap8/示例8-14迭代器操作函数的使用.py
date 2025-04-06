lst=[54,56,77,4,567,34]
# (1)排序操作
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print(lst)
print(asc_lst)
print(desc_lst)

# (2) reversed 反向操作
new_lst=reversed(lst)
print(type(new_lst)) #<class 'list_reverseiterator'>
print(list(new_lst)) # 原类型是一个反相器对象，需要转换类型才能查看结果

# (3) zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y) #打包时，以短的为主，也就是会保留4个元素
print(type(zipobj)) # <class 'zip'>
print(list(zipobj)) # 原类型是一个zip对象，需要转换类型才能查看

# (4) enumerate
enum=enumerate(y,start=1)
print(type(enum)) # <class 'enumerate'>
print(tuple(enum)) # 原类型是一个enumerate对象，需要转换类型才能查看

# (5) all 判断是否所有元素布尔值都是True
lst2=[10,20,'',30]
print(all(lst2)) # False
print(all(lst)) # True

# (6) any 判断是否有一个元素的布尔值为True
print(any(lst2)) # True

# (7) next 获取迭代器的下一个元素，不需要转换类型
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y) #打包时，以短的为主，也就是会保留4个元素
print(next(zipobj)) # ('a', 10) 获取迭代器的下一个元素，不需要转换类型
print(next(zipobj)) # ('b', 20)
print(next(zipobj)) # ('c', 30)

# (8) filter:将所有元素通过函数进行过滤（保留结果为True的），得到一个迭代器对象
def fun(num):
    return num%2==1 # 可能是True，可能是False
obj=filter(fun,range(10)) #函数作为参数，不是函数调用。将range(10),0-9都执行一次fun操作
print(list(obj))  #[1, 3, 5, 7, 9] # 使用filter做一个判断，将这个整数序列中的每个元素都执行一遍fun函数，将结果为True的留下来

# (9) map:将所有元素通过函数进行转换，得到一个迭代器对象
def upper(s):
    return s.upper()

new_lst3=['hello','world','python']
obj2=map(upper,new_lst3)
print(list(obj2))