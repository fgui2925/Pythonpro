print('北京')#没有修改结束符\n，所以，print之后会有一个换行
print('北京',end='-->')#将结束符\n修改为-->，所以，print之后不会换行
print('欢迎你')#没有修改结束符\n，所以，print之后会有一个换行

#print函数完整的语法格式：
#print(value,...,sep='',end='\n',file=None)
#sep是空格的意思，用' '表示，print函数默认带的
#end是结束的意思，用'\n'表示，print函数默认带的
#file是文件的意思，print函数默认是将结果输出到文件中的，文件名默认是缺省的，若定义了文件名，则表示把print的内容写入到文件中