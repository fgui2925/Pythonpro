# 如果两个模块中有同名的函数，后导入的模块的函数将会覆盖先导入的函数。如果要使用，只能使用模块名称打点调用

from my_info import *
from introduce import *

# 导入的两个模块中，具有同名的变量和函数,后导入的会将之前导入的进行覆盖
info()

# 如果不想覆盖，解决方案，可以使用import
import my_info
import introduce
# 使用模块中的函数或变量时，模块名打点调用
my_info.info()
introduce.info()