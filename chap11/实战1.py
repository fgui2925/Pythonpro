import random
import os
import os.path

def my_writes(num,path):
    filename=''
    type_lst=['肉蛋','水果','粮油','烟酒','蔬菜']
    num_lst=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    for i in range(1,num+1):
        if i <10:
            filename='000'+str(i)
        elif i<100:
            filename='00'+str(i)
        elif i<1000:
            filename='0'+str(i)
        else:
            filename=str(i)
        filename+='_'+random.choice(type_lst)
        s=''
        for j in range(9):
            s+=random.choice(num_lst)
        filename+='_'+s
        filename+='.txt'
        with open(os.path.join(path,filename),'w',encoding='utf-8') as f:
            pass
    print('创建完成！')

if __name__ == '__main__':
    path=r'.\data'
    if not os.path.exists(path):
        os.mkdir(path)
    num=3000
    my_writes(num,path)