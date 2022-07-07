import os
from multiprocessing import Process
from time import sleep


def task1(s,name):    #定义的任务1
    while True:
        sleep(s)
        print("这是任务一。。。。。。。。",os.getpid(),"-----",os.getppid(),name)

def task2(s,name):    #定义的任务2
    while True:
        sleep(s)
        print("这是任务二。。。。。。。。",os.getpid(),"-----",os.getppid(),name)

number = 1

if __name__ == '__main__':
    print(os.getpid())
    p = Process(target=task1,name="任务一",args=(1,"aa"))
    p.start()    #启动进程
    print(p.name)    #输出进程的名字
    p1 = Process(target=task2,name="任务二",args=(2,"bb"))
    p1.start()    #启动进程
    print(p1.name)    #输出进程的名字

    while True:
        number +=1
        sleep(0.2)
        if number == 50:
            p.terminate()    #结束进程
            p1.terminate()   #结束进程
            break
        else:print("当前number的值%d"%number)
    print("进程结束")

