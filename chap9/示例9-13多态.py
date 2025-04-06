class Person:
    def eat(self):
        print('人，吃五谷杂粮')

class Cat:
    def eat(self):
        print('猫，喜欢吃鱼')

class Dog:
    def eat(self):
        print('狗，喜欢啃骨头')

# 这三个类中都一个同名的方法，eat

# 编写函数
def fun(obj): # obj是函数的形式参数，在定义处不知道这个形参的数据类型
    obj.eat() # 通过变量obj(对象)调用eat方法

# 创建三个类的对象
person=Person()
cat=Cat()
dog=Dog()

# 调用fun函数
fun(person) #python中的多态，不关心对象的数据类型，只关心对象是否有同名方法
fun(cat)
fun(dog)