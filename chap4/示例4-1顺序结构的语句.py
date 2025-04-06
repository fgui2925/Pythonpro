# 赋值运算符的顺序 从右到左
a=b=c=d=100 #链式赋值
print(a,b,c,d)
a,b,c,d='room'#字符串分解赋值
print(a,b,c,d)

#输入输出语句也是典型的顺序结构
name=input('请输入您的姓名：')
age=eval(input('请输入您的年龄:'))
print('姓名',name)
print('年龄',age)