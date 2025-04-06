import time
now=time.time() # 获取当前时间戳
print(now)

obj=time.localtime() # struct_time对象
print(obj)

obj2=time.localtime(59) # 59秒 默认从1970年1月1日8点0分0秒开始算
print(obj2)

print('年份:',obj2.tm_year)
print('月份:',obj2.tm_mon)
print('日期:',obj2.tm_mday)
print('时:',obj2.tm_hour)
print('分:',obj2.tm_min)
print('秒:',obj2.tm_sec)
print('星期:',obj2.tm_wday) # [0,6] 3的话表示的是星期四
print('年的第多少天:',obj2.tm_yday)

print(time.ctime()) # 时间戳对应的易读的字符串 Tue Dec 17 15:27:45 2024

# 日期时间格式化：struct_time转成字符串格式
print(time.strftime('%Y-%m-%d',time.localtime())) #str--字符串 f---format格式化
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print(time.strftime('月份的名称:%B',time.localtime()))
print(time.strftime('星期的名称:%A',time.localtime()))

# 字符串转成struct_time格式
print(time.strptime('2008-08-08','%Y-%m-%d'))

time.sleep(5) # 休眠5秒

print('hello world')
