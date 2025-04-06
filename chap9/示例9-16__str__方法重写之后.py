class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 方法重写
    def __str__(self):
        return '这是一个人类，具有name和age两个实例属性' # 返回值是一个字符串
per=Person('陈梅梅',20)
print(per) # 输出的还是内存地址码？不是，而是__str__方法中的内容 直接输出对象名，实际上是调用__str__方法
print(per.__str__()) # 手动调用