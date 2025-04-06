from multiprocessing import Queue
if __name__ == '__main__':
    q = Queue(3)
    # 入队
    q.put('hello') # block=True
    q.put('world')
    q.put('python')

    q.put('html',block=True,timeout=2) #等待2秒时候，队列还没有空位置就抛异常
