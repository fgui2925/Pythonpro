print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('-'*40) # 字符串相乘，让字符串'-'出现40次

print(8>7 and 6>5) #True
print(8>7 and 6<5) #False
print(8<7 and 10/0) #False 10/0并没有运算，当第一个表达式结果为False，直接得结果，不会计算and右侧的表达式
print('-'*40)

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print('-'*40)

print(8>7 or 10/0) #True 10/0并没有运算，当第一个表达式结果为True，直接得结果，不会计算or右侧的表达式
print('-'*40)

print(not True)
print(not False)
print(not 8>7)