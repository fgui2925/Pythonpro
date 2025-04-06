# 访问类的私有属性或方法，其实非常不推荐用 stu._Student__fun2()这样的方式去调用
# 访问类的私有属性或方法，建议使用装饰器@property,将一个方法转换成属性去使用。在访问时只能访问属性的值，却不能修改属性的值
# 如果想修改属性的值，需要再设置一个setter

class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender  #私有的实例属性

    # 使用@property 修改方法，将方法转成属性使用
    @property
    def gender(self):
        return self.__gender

    # 将gender这个属性设置为可写属性
    @gender.setter
    def gender(self, value):
        if value != '男' or value != '女':
            self.__gender = '女'
            print('性别有误，已默认设置为女')
        else:
            self.__gender = value


stu = Student('cmm', '女')
print(stu.name, '的性别是', stu.gender)  #stu.gender就会去执行stu.gender()这个方法

# 尝试修改属性值
# stu.gender='男' # AttributeError: property 'gender' of 'Student' object has no setter

stu.gender = '其他'
print(stu.name, '的性别是:', stu.gender)
