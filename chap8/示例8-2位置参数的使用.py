def happy_birthday(name, age):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')
# 调用
# happy_birthday('张三') # TypeError: happy_birthday() missing 1 required positional argument: 'age'
# happy_birthday(18,'张三') # TypeError: can only concatenate str (not "int") to str
happy_birthday('张三',18)