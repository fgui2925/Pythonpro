class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
# 创建类的对象
a=A()
b=B()
c=C('cmm',20)

# 查看对象的属性字典
print(a.__dict__)
print(b.__dict__)
print(c.__dict__)

# 查看对象所属的类
print(a.__class__)
print(b.__class__)
print(c.__class__)

# 查看类的父类元组，结果是元组形式
print(A.__bases__)
print(B.__bases__)
print(C.__bases__)

# 查看类的父类
print(A.__base__)
print(B.__base__)
print(C.__base__) # 如果继承了N个父类，只显示第一个父类

# 查看类的层次结构，结果是元组形式
print(A.__mro__)
print(B.__mro__)
print(C.__mro__) #C类继承了A类，B类，间接继承了object类

# 查看类的子类列表：不是属性调用，是方法调用，有括号。结果是列表形式
print(A.__subclasses__())
print(B.__subclasses__())
print(C.__subclasses__())

