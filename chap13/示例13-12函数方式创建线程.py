import threading
from threading import Thread
import time
# 编写函数
def test():
    for i in range(3):
        time.sleep(1)
        print(f'线程:{threading.current_thread().name}正在执行{i}')

if __name__ == '__main__':
    start = time.time()
    print('主线程开始运行')

    # 线程
    lst=[Thread(target=test) for i in range(2)]

    for item in lst:# item对象类型是Thread
        # 启动线程
        item.start()

    for item in lst:
        item.join()

    print(f'一共耗时：',time.time() - start)

    # 3个线程并行执行的任务是什么？
    # 主线程负责执行main中的代码
    # Thread-1线程，执行3次循环，Thread-2线程，执行3次循环
    # 3个线程又是并发执行，特别是Thread-1和Thread-2谁先执行不一定