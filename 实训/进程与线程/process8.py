#进程间通信

from multiprocessing import Queue
from multiprocessing import Process
from time import sleep

def download(q):
    images =["girl.jpg","boy.jpg","man.jpg"]
    for image in images:
        print("正在下载:",image)
        sleep(0.5)
        q.put(image)    #添加到队列中

def getfile(q):
    while True:
        try:
            file = q.get(timeout = 5)    #的到队列      若没有队列五秒后报错
            print("{}保存成功".format(file))
        except:
            print("全部保存完毕！")
            break


if __name__ == '__main__':
    q = Queue(5)   #创建进程队列

    p1 = Process(target=download,args=(q,))    #启动进程
    p2 = Process(target=getfile,args=(q,))

    p1.start()
    p1.join()   #插队
    p2.start()
    p2.join()