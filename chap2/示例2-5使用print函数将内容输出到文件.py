fp=open('note.txt','w')#打开文件 w-->write
print('北京欢迎你',file=fp)#将“北京欢迎你”输出（写入）到note.txt文件中
fp.close()#关闭文件

#print函数完整的语法格式：
#print(value,...,sep='',end='\n',file=None)
#sep是空格的意思，用' '表示，print函数默认带的
#end是结束的意思，用'\n'表示，print函数默认带的
#file是文件的意思，print函数默认是将结果输出到文件中的，文件名默认是缺省的，若定义了文件名，则表示把print的内容写入到文件中