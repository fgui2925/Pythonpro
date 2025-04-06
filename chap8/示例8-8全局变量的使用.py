a=100 # 全局变量

def calc(x,y):
    return a+x+y

print(a)
print(calc(10,20))
print('-'*50)

def calc2(x,y):
    a=200 # 局部变量名称与全局变量相同
    return a+x+y # a是局部变量。当局部变量名称与全局变量相同时，局部变量的优先级高
print(a)
print(calc2(10,20))
print('-'*50)

def calc3(x,y):
    global s # s使用了关键字global声明，因此是全局变量
    s=300 # 声明和赋值，必须是分开执行
    return s+x+y

print(calc3(10,20))
print(s)