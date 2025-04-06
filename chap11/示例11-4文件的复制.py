def copy(src,new_path):
    # 文件的复制就是边读边写操作
    # (1)打开原文件
    file1=open(src,'rb')
    # (2)打开目标文件
    file2=open(new_path,'wb')
    # (3)开始复制，边读边写
    s=file1.read() #原文件读取所有
    file2.write(s) #向目标文件写入所有
    # (4) 关闭:先打开的后关，后打开的先关
    file2.close()
    file1.close()

if __name__ == '__main__':
    src='./google.jpg' # . 代表的是当前目录
    new_path='../chap10/copy_google.jpg' # ..代表的是上一级目录，相当于windows的后退
    copy(src,new_path)
    print('文件复制完毕')