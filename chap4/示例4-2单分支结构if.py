number=eval(input('请输入您的6位兑奖号码：'))
if number==987654: # 等值判断
    print("恭喜您中奖了！")
if number!=987654: # 不等值判断
    print("很遗憾您未中奖。")

#------以上if判断的表达式，是通过比较运算符计算出来的，结果值是布尔类型-----

n=98
if n%2:  # 98%2的余数是0,0的布尔值是False，非0的布尔值为True
    print('n是奇数')  # 由于98%2的余数是0，所以该行代码不执行
if not n%2:  # 98%2的余数是0,0的布尔值是False，not False的结果是True
    print('n是偶数')

#-----判断一个字符串是否是空字符串-----------
string=input('请输入一个字符串：')
if string:
    print('您输入的是一个非空字符串')
if not string:
    print('您输入的是一个空字符串')

#-----表达式也可以是一个单纯的布尔型变量-----
flag=eval(input('请输入一个布尔型的值：True或False'))
if flag:
    print('flag的值为True')
if not flag:
    print('flag的值为False')

#-----使用if语句时，如果语句块中只有一句代码，可以将语句块直接写在冒号后面-----
a=10
b=5
if a>b:max=a #语句块只有一句，赋最大值
print('a和b的最大值为：',max)

#if a>b:max=a print(max)   #SyntaxError: invalid syntax
