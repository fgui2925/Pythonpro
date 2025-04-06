class Cpu:
    pass

class Disk:
    pass

class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu=Cpu() # 定义一个Cpu对象
disk=Disk() # 定义一个Disk对象
com=Computer(cpu,disk) # 定义一个Computer对象，并用cpu和disk进行传参
com1=com # 变量（对象）的赋值
print(com) # 直接输出类对象的时候会输出内存地址，因为自动调用了object类的_str_()方法
print(com1)
print(com.cpu,com.disk)   # 子对象的内存地址
print(com1.cpu,com1.disk)
print('-'*40)

import copy
com2=copy.copy(com) # 浅拷贝，会产生一个新的对象com2(新的内存地址)，但是子对象不变
print(com,com.cpu,com.disk)
print(com2,com2.cpu,com2.disk)
print('-'*40)

com3=copy.deepcopy(com) # 深拷贝，会产生一个新的对象com3，以及新的子对象cpu,disk(新的内存地址)
print(com,com.cpu,com.disk)
print(com3,com3.cpu,com3.disk)

