#池子
#非阻塞式


from multiprocessing import Pool
import time
import os
from random import random


def task(task_name):
    print("开始做任务啦！",task_name)
    start = time.time()
    time.sleep(random()*2)
    end = time.time()
    #print()
    return "完成任务:{}!用时:{},进程id:{}".format(task_name,(end-start),os.getpid())

container = []


def callback_func(n):   #定义的回调函数   接收return "完成任务:{}!用时:{},进程id:{}".format(task_name,(end-start),os.getpid())返回的值
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)    #创建进程池

    tasks = ["听音乐","吃饭","洗衣服","打游戏","散步","看孩子","做饭"]

    for task1 in tasks:
        pool.apply_async(task,args=(task1,),callback=callback_func)    #apply_async  非阻塞式

    pool.close()   #添加任务结束
    pool.join()   #阻碍   任务结束后自动消除

    for c in container:   #输出回调的值
        print(c)

    print("over!!")