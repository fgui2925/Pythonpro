from multiprocessing import Pool
import time,os
# 编写任务
def task(name):
    print(f'子进程的pid：{os.getpid()},执行的任务：{name}')
    time.sleep(1)

if __name__ == '__main__':
    # 主进程
    start = time.time()
    print('主进程开始运行')
    pool = Pool(3)
    # 创建任务
    for i in range(10):
        # 以非阻塞的方式
        pool.apply_async(task, args=(i,))

    pool.close() # 关闭进程池不再接收新任务
    pool.join() # 阻塞主进程
    print('所有子进程执行完毕,父进程执行结束')
    print(time.time()-start)
