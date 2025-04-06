s='HelloWorld'
# 字符串的替换
new_s=s.replace('o','你好',1)# 最后一个参数是替换次数，默认是全部替换
print(new_s)

# 字符串在指定的宽度范围内居中
print(s.center(20))
print(s.center(20,'*'))

# 去掉字符串左右的空格
s='    Hello    World    '
print(s.strip()) #去除字符串左侧和右侧的空格
print(s.lstrip()) #去除字符串左侧的空格
print(s.rstrip()) #去除字符串右侧的空格

# 去掉字符串左右侧指定的字符
s3='dlddlHdl-Hello-ld-World'
print(s3.strip('ld')) #去除字符时与顺序无关
print(s3.lstrip('dl'))
print(s3.rstrip('dl'))