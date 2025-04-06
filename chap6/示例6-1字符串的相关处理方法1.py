s1='HelloWorld'

# 将字符串的字符全部转为大写，结果为一个新的字符串
new_s2=s1.upper()
print(new_s2)

# 将字符串的字符全部转为小写，结果为一个新的字符串
new_s3=s1.lower()
print(new_s3)

#字符串的分隔
e_mail='gf2211@163.com'
lst=e_mail.split(sep='@')
print('邮箱名:',lst[0],'邮件服务器名:',lst[1])

# 统计字符串中字符的出现次数
print(s1.count('o'))

# 检索操作：检索字符在字符串中首次出现的索引位置
print(s1.find('o'))
print(s1.find('p'))  #-1表示没找到

print(s1.index('o'))
# print(s1.index('p'))  #ValueError: substring not found

# 判断字符串前缀和后缀
print(s1.startswith('H')) #True
print(s1.startswith('P')) #False

print('demo.py'.endswith('.py')) #True
print('text.txt'.endswith('.txt')) #True
