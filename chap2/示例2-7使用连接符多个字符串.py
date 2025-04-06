print('北京欢迎你','2023')
print('北京欢迎你'+'2023')
print('北京欢迎你'+2023)#TypeError: can only concatenate str (not "int") to str
#注意，连接符+只能连接字符串，不能连接字符串和其他类型的字符（如数字）等。否则会报错

#print函数完整的语法格式：
#print(value,...,sep='',end='\n',file=None)
#sep是空格的意思，用' '表示，print函数默认带的
#end是结束的意思，用'\n'表示，print函数默认带的
#file是文件的意思，print函数默认是将结果输出到文件中的，文件名默认是缺省的，若定义了文件名，则表示把print的内容写入到文件中