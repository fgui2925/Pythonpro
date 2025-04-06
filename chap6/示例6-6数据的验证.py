# isdigit()识别十进制的阿拉伯数字
print('123'.isdigit()) #True。认阿拉伯数字
print('一二三'.isdigit())  #False。不认中文的数字
print('0b1010'.isdigit())  #False。不认二进制数
print('ⅠⅡⅢ'.isdigit())  #False。不认罗马数字
print('-'*50)

# isnumeric()识别所有类型的数字
print('123'.isnumeric()) #True。认阿拉伯数字
print('一二三'.isnumeric())  #True。认中文的数字
print('0b1010'.isnumeric())  #False。不认二进制数
print('ⅠⅡⅢ'.isnumeric())  #True。认罗马数字
print('壹贰叁'.isnumeric())  #True。认识中文的大写数字
print('-'*50)

# isalpha()判断所有字符都是字母（包含中文字符）
print('hello你好'.isalpha())  #True
print('hello你好123'.isalpha())  #False
print('hello你好一二三'.isalpha())  #True
print('hello你好ⅠⅡⅢ'.isalpha())  #False
print('hello你好壹贰叁'.isalpha())  #True
print('-'*50)

# isalnum()判断所有字符都是数字或字母
print('hello你好'.isalnum())  #True
print('hello你好123'.isalnum())  #False
print('hello你好一二三'.isalnum())  #True
print('hello你好ⅠⅡⅢ'.isalnum())  #False
print('hello你好壹贰叁'.isalnum())  #True
print('-'*50)

# islower()、isupper()判断字符的大小写(中文既是大写又是小写)
print('HelloWorld'.islower()) #False
print('helloworld'.islower()) #True
print('hello你好'.islower()) #True
print('-'*50)
print('HelloWorld'.isupper()) #False
print('HELLOWORLD'.isupper()) #True
print('HELLO你好'.isupper()) #True
print('-'*50)

# istitle()判断所有字符都是首字母大写
print('Hello'.istitle()) #True
print('HelloWorld'.istitle()) #False
print('Helloworld'.istitle()) #True
print('Hello World'.istitle()) #True
print('Hello world'.istitle()) #False
print('-'*50)

# isspace()判断所有字符都是空白字符
print('\t'.isspace()) #True
print(' '.isspace()) #True
print('\n'.isspace()) #True