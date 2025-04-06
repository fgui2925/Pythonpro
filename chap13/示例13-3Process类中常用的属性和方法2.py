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
        p1=Process(target=sub_process,args=('gf',)) # 没有指定target参数时，不会执行自己编写的函数中的代码，会调用执行Process类中run方法
        # 创建第二个子进程
        p2 = Process(target=sub_process2,args=('zs',))
        # 调用start()启动子进程
        p1.start() # 没有指定target参数时，调用Process类中的run方法
        p2.start()

        # 终止进程
        p1.terminate()
        # p2.terminate()

    print('主进程执行结束')