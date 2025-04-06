from multiprocessing import Process
import os,time
# 函数中的代码是进程要执行的代码
def test():
    print(f'我是子进程，我的pid是{os.getpid()}，我的父进程是:{os.getppid()}')
    time.sleep(1)

if __name__ == '__main__':
    print('主进程开始执行')
    lst=[]
    # 创建五个子进程
    for i in range(5):
        p=Process(target=test)
        # 启动子进程
        p.start()
        # 启动中的进程添加到列表中
        lst.append(p)
    # 遍历lst，列表中五个子进程
    for p in lst: # p的数据类型是 Process类型
        p.join() # 阻塞主进程

    print('主进程运行结束')
    # 主进程要等到所有子进程执行结束才会继续执行