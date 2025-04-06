from datetime import datetime
from datetime import timedelta

# 创建两个datetime对象
dt1=datetime(2028,10,1)
dt2=datetime(2028,5,1)
delta1=dt1-dt2
print(type(delta1),delta1)
print('2028年5月1日之后的153天是:',datetime(2028,5,1)+delta1)

# 通过传入参数的方式创建一个timedelta对象
delta2=timedelta(10)
print('创建一个10天的timedelta对象',delta2)
delta3=timedelta(10,11)
print('创建一个10天11秒的timedelta对象',delta3)
delta4=timedelta(10,11,hours=20)
print(delta4)