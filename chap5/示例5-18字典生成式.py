# (1)使用d={key:value for key in range()}创建字典
import random
d={item:random.randint(1,100) for item in range(4)}
print(d)

# （2）使用d={key:value for key,value in zip(lst1,lst2)}创建字典
lst1=[1001,1002,1003]
lst2=['张三','李四','王五']
d={key:value for key,value in zip(lst1,lst2)}
print(d)
