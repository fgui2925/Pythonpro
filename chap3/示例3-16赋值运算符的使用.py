x=20
y=10
x+=y #等同于x=x+y，可以简写为左侧的表达式
print(x,type(x))

x=20
y=10
x-=y #等同于x=x-y，可以简写为左侧的表达式
print(x,type(x))

x=20
y=10
x*=y #等同于x=x*y，可以简写为左侧的表达式
print(x,type(x))

x=20
y=10
x//=y #等同于x=x//y，可以简写为左侧的表达式
print(x,type(x))

x=20
y=10
x/=y #等同于x=x/y，可以简写为左侧的表达式
print(x,type(x))

x=20
y=10
x%=y #等同于x=x%y，可以简写为左侧的表达式
print(x,type(x))

x=2
y=10
x**=y #等同于x=x**y，可以简写为左侧的表达式
print(x,type(x))

# python中支持链式赋值
a=b=c=100 #相当于执行 a=100 b=100 c=100
print(a,b,c)

#python支持系列解包赋值
a,b=10,20 #相当于执行 a=10 b=20
print(a,b)

print('----------如何交换两个变量的值呢--------')
a,b=b,a #将a的值赋给b，将b的值赋给a
print(a,b)