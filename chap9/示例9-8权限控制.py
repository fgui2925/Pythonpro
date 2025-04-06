class Student:
    # 首尾双下划线，表示特殊的方法
    def __init__(self,name,age,gender):
        self._name=name # 单下划线开头，表示受保护的，只能本类和子类访问
        self.__age=age # 双下划线开头，表示私有的，只能本类去访问
        self.gender=gender # 普通的实例属性，类的内部、外部，及子类都可以访问

    def _fun1(self):
        print('子类和本身可以使用')

    def __fun2(self):
        print('只有本类可以使用')

    def show(self): # 普通的实例方法
        self._fun1() # 类本身访问受保护的方法
        self.__fun2() # 类本身访问私有方法
        print(self._name) # 类本身访问受保护的实例属性
        print(self.__age) # 类本身访问私有的实例属性

# 创建一个学生类的对象
stu=Student('cmm',20,'女')
# 类的外部
print(stu._name)
# print(stu.__age) # AttributeError: 'Student' object has no attribute '__age'. Did you mean: '_name'?
stu._fun1()
# stu.__fun2() # AttributeError: 'Student' object has no attribute '__fun2'. Did you mean: '_fun1'?

# 私有的实例属性和方法怎么访问？
print(stu._Student__age) # 为什么可以这样访问呢？
stu._Student__fun2()

print(dir(stu)) # dir()提取出类的所有的属性和方法