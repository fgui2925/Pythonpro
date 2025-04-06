from datetime import datetime # 从datetime模块中导入datetime类
dt=datetime.now() #获取当前的系统时间
print(dt)

# datetime是一个类，手动创建这个这个类的对象
dt2=datetime(2028,8,8,20,8)
print(type(dt2),dt2)
print('年',dt2.year,'月:',dt2.month,'日:',dt2.day,'时:',dt2.hour,'分:',dt2.minute,'秒:',dt2.second)

# 比较两个datetime类型对象的大小
laber_day=datetime(2028,5,1,0,0,0)
national_day=datetime(2028,10,1,0,0,0)
print('2028年5月1日比2028年10月1日早吗？',laber_day<national_day)

# datetime类型转为字符串类型
nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y-%m-%d %H:%M:%S')
print(type(nowdt),nowdt)
print(type(nowdt_str),nowdt_str)

# 字符串类型转为datetime类型
str_datetime='2028年8月8日 20点8分'
dt3=datetime.strptime(str_datetime,'%Y年%m月%d日 %H点%M分')
print(type(dt3),dt3)