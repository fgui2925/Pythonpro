from multiprocessing import Process
import os,time
# 函数式方式创建子进程
def sub_process(name):
    print(f'子进程PID:{os.getpid()}，父进程的PID：{os.getppid()},---------{name}')
    time.sleep(1)

def sub_process2(name):
    print(f'子进程PID:{os.getpid()}，父进程的PID：{os.getppid()},---------{name}')
    time.sleep(1)

if __name__ == '__main__':
    # 主进程
    print('主进程开始执行')
    for i in range(5):
        # 创建第一个子进程
        p1=Process(target=sub_process,args=('gf',))
        # 创建第二个子进程
        p2 = Process(target=sub_process2, args=('zs',))
        # 调用start()启动子进程
        p1.start()
        p2.start()
        print(p1.name,'在运行中吗',p1.is_alive())
        print(p2.name,'在运行中吗', p2.is_alive())

        print(p1.name,'pid是',p1.pid)
        print(p2.name,'pid是',p2.pid)

        p1.join() # 阻塞主进程，主进程要等p1运行结束
        p2.join()

        print(p1.name, '在运行中吗', p1.is_alive())
        print(p2.name, '在运行中吗', p2.is_alive())

    print('主进程运行结束')