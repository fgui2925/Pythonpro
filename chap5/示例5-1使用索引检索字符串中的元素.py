# s[] 方括号获取字符串变量s中的元素。
#正向递增
s='helloworld'
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')
print("\n-----------------")

# 反向递减
for i in range(-len(s),0):
    print(i,s[i],end='\t')
print("\n-----------------")

print(s[9],s[-1])