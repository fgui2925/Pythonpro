import re #导入

# match函数，查找字符串的开头是否符合pattern
pattern = r'\d\.\d+'  # +限定符，\d 0-9数字出现1次或多次  #当在字符串开头加上r或R，表示原始字符串，不进行任何转义
s = "I study Python 3.11 every day"  # 待匹配字符串
match = re.match(pattern, s, re.I)
print(match)  # None
s2 = "3.11Python I study every day"
match2 = re.match(pattern, s2)
print(match2)  #<re.Match object; span=(0, 4), match='3.11'>
print('匹配值的起始位置:',match2.start())
print('匹配值的结束位置:',match2.end())
print('匹配值的位置区间:',match2.span())
print('待匹配的字符串:',match2.string)
print('匹配的数据:',match2.group())