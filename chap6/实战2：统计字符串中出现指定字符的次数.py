s='HelloPython,Hellojava,hellophp'
x=input('请输入要统计的字符:')
s1=s.lower()
x1=x.lower()
d=s1.count(x1)
print('%s在%s中一共出现了%d次'%(x,s,d))   #字符串格式化1
print(f'{x}在{s}中一共出现了{d}次')   #字符串格式化2
print('{0}在{1}中一共出现了{2}次'.format(x,s,d))   #字符串格式化3