import os
print('当前的工作路径:',os.getcwd()) # cwd:current working directory
lst=os.listdir()
print('当前路径下的所有目录及文件',lst)
print('指定路径下的所有目录及文件',os.listdir('D:/pythonpro'))
# 创建目录
# os.mkdir('好好学习') # 如果创建的文件夹存在，程序会报错：FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: '好好学习'
# 创建多级目录
# os.makedirs('./aa/bb/cc')  # 如果创建的文件夹存在，程序会报错

# 删除目录
# os.rmdir('./好好学习') # 如果要删除的目录找不到会报错
# 删除多级目录
# os.removedirs('./aa/bb/cc') # 如果要删除的目录找不到会报错

# 设置当前路径
os.chdir('D:/pythonpro') #change directory
print('当前的工作路径:',os.getcwd()) # 再写代码，就从当前路径D:/pythonpro出发了

# 遍历目录树,相当于递归操作
for dirs,dirlst,filelst in os.walk('D:/pythonpro'):
    print(dirs) # 路径
    print(dirlst) # 路径下的目录清单
    print(filelst) # 路径下的文件清单
    print('-'*40)