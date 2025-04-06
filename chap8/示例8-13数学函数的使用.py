print('绝对值:',abs(100),abs(-100),abs(0))
print('商和余数:',divmod(13,4))
print('最大值',max('hello'))
print('最大值',max([10,4,56,78,4]))
print('最小值',min('hello'))
print('最小值',min([10,4,56,78,4]))

print('求和',sum([10,20,30]))
print('x的y次幂',pow(2,3))

print(round(3.1415926)) #round只有一个参数，四舍五入保留整数
print(round(3.9415926))
print(round(3.1415926,2))
print(round(3.9415926,3))
print(round(314.15926,-1)) # -1表示对个位上的数进行四舍五入，0表示对小数进行四舍五入
print(round(314.15926,-2)) # -2表示对十位上的数进行四舍五入