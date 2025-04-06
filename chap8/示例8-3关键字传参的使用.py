def happy_birthday(name, age):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

# 关键字传参
happy_birthday(age=18,name='张三')
# happy_birthday(age=18,name1='张三') #TypeError: happy_birthday() got an unexpected keyword argument 'name1'. Did you mean 'name'

happy_birthday('张三',age=18) # 正常执行，可以用位置传参+关键字传参
# happy_birthday(name='张三',18) # SyntaxError: positional argument follows keyword argument

# 既有位置传参又有关键字传参时，需要遵循：位置传参在前，关键字传参在后