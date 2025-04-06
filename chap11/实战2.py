import os
import os.path

def creat_dirs(num,path):
    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(1,num+1):
        if not os.path.exists(os.path.join(path,str(i))):
            os.mkdir(os.path.join(path,str(i)))
    print('创建完成！')

if __name__ == '__main__':
    path_data=r'.\newdir'
    num_data=eval(input('请输入要创建的文件夹个数：'))
    creat_dirs(num_data,path_data)