from multiprocessing import Queue
if __name__ == '__main__':
    q = Queue(3)
    # 入队
    q.put('hello')
    q.put('world')
    q.put('python')

    q.put('html')