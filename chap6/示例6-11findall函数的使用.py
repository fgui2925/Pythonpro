import re

# findall函数，查找字符串中所有符合pattern的内容
pattern=r'\d.\d+'
s = "I study Python3.11 every day Python2.7"  # 待匹配字符串
s2='4.10 Python I study every day'
s3='I study Python every day'

lst=re.findall(pattern,s)
print(lst)
lst2=re.findall(pattern,s2)
print(lst2)
lst3=re.findall(pattern,s3)
print(lst3)