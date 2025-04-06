from threading import Thread
a=100 # 全局变量

def add():
    print('加线程开始执行')
    global a
    a+=30
    print('a=',a)
    print('加线程执行完毕')

def sub():
    print('减线程开始执行')
    global a
    a-=50
    print('a=',a)
    print('减线程执行完毕')

if __name__=='__main__':
    # 主线程
    print('主线程开始执行')
    print('a=', a)
    p1 = Thread(target=add)
    p2 = Thread(target=sub)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('主线程执行完毕')
    print('a=',a)