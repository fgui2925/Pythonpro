s='helloworld'
# in的使用
print('e在helloworld中存在吗？','e'in s)
print('v在helloworld中存在吗？','v'in s)

# not in的使用
print('e在helloworld中不存在吗？','e'not in s)
print('v在helloworld中不存在吗？','v'not in s)

# 内置函数的使用
print('len(helloword)',len(s))
print('max(helloword)',max(s)) #按ASCII码值计算
print('min(helloword)',min(s))

#序列对象的方法，使用序列的名称，打点调用
print('s.index()',s.index('o'))
print('s.count()',s.count('l'))