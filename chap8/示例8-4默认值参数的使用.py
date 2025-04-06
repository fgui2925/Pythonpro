def happy_birthday(name='张三', age=18):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

# 调用
happy_birthday() # 不传参
happy_birthday('李四') # 位置传参
happy_birthday(age=19)  #关键字传参，name采用默认值

# happy_birthday(19) #19被传给了name
# TypeError: can only concatenate str (not "int") to str

# 同时存在位置参数和默认值参数时，应当遵循：位置参数在前，默认值参数在后
def fun(a,b=20):  #a做位置参数，b做默认值参数
    pass
# def fun(a=20,b)  # 同时存在位置参数和默认值参数时，位置参数在后会报语法错误。 SyntaxError: parameter without a default follows parameter with a default
#     pass