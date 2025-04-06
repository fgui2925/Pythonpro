class Person: # 默认继承了object
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'大家好，我叫:{self.name},今年:{self.age}岁')

# Student继承Person类
class Student(Person):
    def __init__(self,name,age,stuno):
        super().__init__(name,age) # 调用父类的初始化方法
        self.stuno = stuno

    def show(self):
        super().show()  # 调用父类中的方法
        print(f'我的学号是{self.stuno}')

# Doctor继承Person类
class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department = department

    def show(self):
        # super().show()  # 调用父类中的show()方法
        print(f'我叫:{self.name},我的年龄是{self.age},我工作的科室是:{self.department}')

stu=Student('cmm',18,'1001')
stu.show() # 调用子类自己的show()方法

doc=Doctor('zyy',32,'外科')
doc.show() # 调用子类自己的show()方法