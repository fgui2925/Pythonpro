import re

# search函数，查找字符串中第一个符合pattern的内容
pattern=r'\d.\d+'
s = "I study Python3.11 every day Python2.7"  # 待匹配字符串
match=re.search(pattern,s) # <re.Match object; span=(14, 18), match='3.11'>
print(match)

s2='4.10 Python I study every day'
match2=re.search(pattern,s2)
print(match2)

s3='I study Python every day'
match3=re.search(pattern,s3)
print(match3)

print(match.group())
print(match2.group())