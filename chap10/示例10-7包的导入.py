import admin.my_admin as a # 包名.模块名 admin是包名，my_admin是模块名
a.info() # 包被导入时，__init__中的内容自动被调用，且只会被调用一次

print('-'*40)
from admin import my_admin as b # from 包名 import 模块名
b.info()

print('-'*40)
from admin.my_admin import info # from 包名.模块名 import 函数名（变量名等）
info()

print('-'*40)
from admin.my_admin import *
print(name)