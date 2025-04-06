def my_read(filename):
    # (1)打开
    file=open(filename,'w+',encoding='utf-8')
    # (2)操作
    file.write('你好啊') # 写入完成，文件指针在最后
    # seek 修改文件指针的位置
    file.seek(0)
    # 读取
    # s=file.read() #读取全部
    # s=file.read(2) # 你好 2指的是两个字符
    # s=file.readline() # 读取一行数据
    # s=file.readline(2) # 你好 读取一行中的2个字符
    # s=file.readlines() # 读取所有，结果为列表类型，一行为列表中的一个元素
    # 读取“好啊”
    file.seek(3) #指针移动3个字节，utf-8，一个中文占3个字节
    s =file.read() #读取指针后边的所有内容
    print(type(s),s)
    # (3)关闭
    file.close()

if __name__ == '__main__':
    my_read('d.txt')