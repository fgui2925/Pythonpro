import os.path
print('获取文件或目录的绝对路径',os.path.abspath('./b.txt'))
print('判断文件或目录在磁盘上是否存在',os.path.exists('./b.txt')) # 相对路径 True
print('判断文件或目录在磁盘上是否存在',os.path.exists('./好好学习')) # False
print('拼接路径：',os.path.join(r'D:\pythonpro\chap11','b.txt')) #D:/pythonpro/chap11\b.txt
print('分割文件的名和文件后缀名：',os.path.splitext('b.txt')) # 元组类型 ('b', '.txt')
print('提取文件名：',os.path.basename(r'D:\pythonpro\chap11\b.txt'))
print('提取文件名：',os.path.dirname(r'D:\pythonpro\chap11\b.txt'))

print('判断一个路径是否是有效路径：',os.path.isdir(r'D:\pythonpro\chap11')) #True
print('判断一个路径是否是有效路径：',os.path.isdir(r'D:\pythonpro\chap110')) #False

print('判断一个文件是否是有效文件：',os.path.isfile(r'D:\pythonpro\chap11\b.txt')) #True
print('判断一个文件是否是有效文件：',os.path.isfile(r'D:\pythonpro\chap11\bbbbb.txt')) #False