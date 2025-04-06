# format()
print(format(3.14,'20')) # 数值型默认右对齐
print(format('hello','20')) # 字符串默认左对齐
print(format('hello','*<20')) # *是填充符 <是左对齐 20是显示的宽度
print(format('hello','*>20'))
print(format('hello','*^20'))

print(format(3.1415926,'.2f'))
print(format(20,'b'))
print(format(20,'o'))
print(format(20,'x'))
print(format(20,'X'))

print('-'*40)
print(len('helloworld'))
print(len([10,20,30,40,50]))

print('-'*40)
print(id(10))
print(id('hello'))
print(type(10))
print(type('hello'))

print(eval('10+30')) #去掉字符串左右的引号
print(eval('10>30'))
