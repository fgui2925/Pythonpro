from multiprocessing import Queue
if __name__ == '__main__':
    # 创建一个队列
    q=Queue(3) #最多可以接受3条信息
    print('队列是否为空：',q.empty()) # True
    print('队列是否为满：',q.full()) # False
    # 向队列中添加信息
    q.put('hello')
    q.put('world')
    print('队列是否为空：',q.empty()) # False
    print('队列是否为满：',q.full()) # False
    q.put('python')
    print('队列是否为空：',q.empty()) # False
    print('队列是否为满：',q.full()) # True
    print('队列当中的信息个数：', q.qsize())

    # 出队
    print(q.get())
    print('队列当中的信息个数：', q.qsize())

    # 入队
    q.put_nowait('html')
    # q.put_nowait('sql') # queue.Full
    # q.put('sql') # 不报错，会一直等待队列有空位
    # 遍历
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait()) # nowait()不等待

    print('队列是否为空：', q.empty()) # True
    print('队列是否为满：', q.full()) # False
    print('队列当中的信息个数：', q.qsize())
