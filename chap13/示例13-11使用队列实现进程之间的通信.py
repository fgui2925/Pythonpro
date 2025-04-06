from multiprocessing import Queue,Process
import time
a=100
def write_msg(q):
    global a
    if not q.full():
        for i in range(6):
            a-=10
            q.put(a)
            print('a入队时的值：',a)

def read_msg(q):
    time.sleep(1)
    while not q.empty():
        print('出队时a的值：',q.get())

if __name__ == '__main__':
    print('主进程开始执行')
    q=Queue() # 由主进程创建队列，没有指定参数，说明可接收的消息个数无上限
    # 创建两个子进程
    p1=Process(target=write_msg,args=(q,))
    p2=Process(target=read_msg,args=(q,))
    # 启动两个子进程
    p1.start()
    p2.start()
    # 阻塞主进程
    p1.join()
    p2.join()
    print('主进程执行完毕')