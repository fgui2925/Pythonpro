def calc(a,b):
    s=a+b
    return s

result=calc(1,2)
print(result)
# print(a,b,s) # a,b是函数的参数，参数是局部变量，s是函数中定义的变量，也是局部变量
# NameError: name 'a' is not defined
