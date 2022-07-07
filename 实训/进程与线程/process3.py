#每个进程独立使用全局变量
import os
from multiprocessing import Process
from time import sleep


m = 1
def task1(s,name):    #定义的任务1
    global m
    while True:
        sleep(s)
        m += 1
        print("这是任务一。。。。。。。。",m)

def task2(s,name):    #定义的任务2
    global m
    while True:
        sleep(s)
        m += 1
        print("这是任务二。。。。。。。。",m)


if __name__ == '__main__':

    p = Process(target=task1,name="任务一",args=(1,"aa"))
    p.start()    #启动进程

    p1 = Process(target=task2,name="任务二",args=(1,"bb"))
    p1.start()    #启动进程

    while True:
        sleep(1)
        m +=1
        print("-----------main",m)





