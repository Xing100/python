import os
from multiprocessing import Process
from time import sleep


def task1():    #定义的任务1
    while True:
        sleep(1)
        print("这是任务一。。。。。。。。",os.getpid(),"-----",os.getppid())

def task2():    #定义的任务2
    while True:
        sleep(1)
        print("这是任务二。。。。。。。。",os.getpid(),"-----",os.getppid())

if __name__ == '__main__':
    print(os.getpid())
    p = Process(target=task1,name="任务一")
    p.start()    #启动进程并执行任务
    print(p.name)
    p1 = Process(target=task2,name="任务二")
    p1.start()   #启动进程并执行任务
    print(p1.name)
