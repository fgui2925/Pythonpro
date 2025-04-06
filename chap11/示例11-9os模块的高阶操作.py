import os
# 删除文件
# os.remove('./a.txt') #要删除的文件不存在时，程序报错
# 重命名
# os.rename('./aa.txt','new_aa.txt')

# 转换时间格式
import time
def date_format(longtime):
    s=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(longtime))
    return s

# 获取文件信息
info=os.stat('./new_aa.txt')
print(type(info),info) #<class 'os.stat_result'>

print('最近一次访问时间:',date_format(info.st_atime))
print('在windows系统中显示的文件创建时间:',date_format(info.st_ctime))
print('最近一次修改时间:',date_format(info.st_mtime))
print('文件的大小(单位是字节):',info.st_size)

# 启动路径下的文件
# os.startfile('calc.exe')
os.startfile(r'D:\Python\Python313\python.exe')