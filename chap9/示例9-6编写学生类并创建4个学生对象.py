class Student:
    # 类属性：定义在类中，方法外的变量
    school='北京***教育'

    #初始化方法__init__
    def __init__(self,xm,age):  #name,age是方法的参数，是局部变量，作用域是整个__init__方法
        self.name=xm # 左侧是实例属性，xm是局部变量，将局部变量的值xm赋值给实例属性self.name
        self.age=age # 实例的名称和局部变量的名称可以相同

    # 定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫:{self.name},年龄是:{self.age}岁')  # 实例属性是可以在整个类当中去使用的

# 根据图纸可以创建出N多个对象
stu=Student('陈梅梅',18)
stu2=Student('马丽',21)
stu3=Student('Marry',25)
stu4=Student('John',23)

print(str(stu))
print(str(stu2))
print(str(stu3))
print(str(stu4))

Student.school='派森教育' # 给类的属性赋值

# 将学生对象存储到列表中
lst=[stu,stu2,stu3,stu4] #列表中的元素使Student类型的对象
for item in lst: # item是列表中的元素，是Student类型的对象
    item.show() #对象名打点调用示例方法
