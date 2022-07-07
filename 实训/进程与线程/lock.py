#线程同步

import threading
from time import sleep


lock = threading.Lock()   #创建锁
list1 = [0]*10

def task1():
    lock.acquire()   #获得一个锁
    for i in range(len(list1)):
        list1[i] = 1
        sleep(0.5)
    lock.release()   #释放锁

def task2():
    lock.acquire()
    for i in range(len(list1)):
        print(i)
        sleep(0.5)
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(list1)
