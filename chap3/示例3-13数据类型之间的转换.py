x=10
y=3
z=x/y
print(z,type(z)) #隐式转换，通过运算隐式的转了结果的类型为浮点数

# float类型转成int类型，只保留整数部分
print('float类型转成int类型',int(3.14))
print('float类型转成int类型',int(3.9))
print('float类型转成int类型',int(-3.14))
print('float类型转成int类型',int(-3.9))

# int类型转成float类型
print('int类型转成float类型',float(10))

# str类型转成int类型
print(int('10')+int('20'))

# 将字符串转成int或float时报错的情况
#print(int('18a')) #ValueError: invalid literal for int() with base 10: '18a'
#print(int('3.14')) #ValueError: invalid literal for int() with base 10: '3.14'
#print(float('45a.987')) #ValueError: could not convert string to float: '45a.987'

#chr()和ord()是一对
print(ord('桂')) #桂在Unicode表中对应的整数值
print(chr(26690)) #整数26690在Unicode表中对应的字符

#进制之间的转换操作，十进制与其他进制之间的转换，转换后的结果是一个字符串类型
print('十进制转成十六进制：',hex(26472))
print('十进制转成八进制：',oct(26472))
print('十进制转成二进制：',bin(26472))