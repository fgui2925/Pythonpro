# 存储和读取一维数组
import csv


def my_write():
    lst=['张三','李四','王五','陈六','麻七']
    with open('student.csv','w') as file:
        file.write(','.join(lst)) # .write方法只能写入字符串，需要将列表转成字符串

def my_read():
    with open('student.csv','r') as file:
        s=file.read()
        lst=s.split(',')
        print(lst)

# 存储和读取二维数据
def my_write_table():
    lst=[
        ['商品名称','单价','采购数量'],
        ['水杯', '98.5', '20'],
        ['鼠标', '89', '100']
    ]
    with open('table.csv','w') as file:
        for row in lst: #row的数据类型是列表类型
            line=','.join(row)
            file.write(line)
            file.write('\n')

def my_read_table():
    data=[]
    with open('table.csv','r') as file:
        lst=file.readlines()
        for line in lst: #line是字符串类型
            lst1=line[:len(line)-1].split(',') #结果是列表
            data.append(lst1)
        print(data)

if __name__ == '__main__':
    # my_write()
    # my_read()
    # my_write_table()
    my_read_table()