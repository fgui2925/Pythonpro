def calc(a,b):
    return a+b

print(calc(1,2))

# 匿名函数
s=lambda a,b:a+b
print(type(s)) #<class 'function'> 函数
# 调用匿名函数
print(s(10,20))
print('-'*50)

# 匿名函数的使用场景：列表取值
# (1)列表正常的取值操作
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])
print('-' * 50)
# (2)使用匿名函数进行取值
for i in range(len(lst)):
    result=lambda x:x[i] # 根据索引取值,result的类型是function ,x是形式参数
    print(result(lst)) # lst是实际参数
print('-'*50)

# 匿名函数的使用场景：排序
student_scores=[
    {'name':'陈梅梅','score':98},
    {'name': '王一一', 'score': 95},
    {'name': '张天乐', 'score': 65},
    {'name': '白雪儿', 'score': 100},
]
# 对列表进行排序，排序规则是按字典中的成绩
student_scores.sort(key=lambda x:x.get('score'), reverse=True)
print(student_scores)

student_scores=sorted(student_scores, key=lambda x:x.get('score'))
print(student_scores)