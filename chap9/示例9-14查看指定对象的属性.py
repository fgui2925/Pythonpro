class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫{self.name},我今年：{self.age}')

# 创建Person类的对象
per=Person('陈梅梅',20) #创建对象时会自动调用__init__方法()
print(dir(per)) # dir()提取出该对象所属的类的所有的属性和方法

print(per) #自动调用了__str__方法，输出对象的描述信息，此处输出的是一个内存地址 <__main__.Person object at 0x00000121B76A56A0>
