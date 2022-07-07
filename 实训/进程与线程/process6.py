#池子
#阻塞模式


from multiprocessing import Pool
import time
import os
from random import random


def task(task_name):
    print("开始做任务啦！",task_name)
    start = time.time()
    time.sleep(random()*2)
    end = time.time()
    print("完成任务:{}!用时:{},进程id:{}".format(task_name,(end-start),os.getpid()))




if __name__ == '__main__':
    pool = Pool(5)    #创建进程池

    tasks = ["听音乐", "吃饭", "洗衣服", "打游戏", "散步", "看孩子", "做饭"]

    for task1 in tasks:
        pool.apply(task,args=(task1,))    #apply  阻塞式


    pool.close()    #添加任务结束
    pool.join()     #阻碍   任务结束后自动消除


    print("over!!!")