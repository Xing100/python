#线程
#状态   创建  就绪  运行   阻塞   结束


import threading
from time import sleep


def download(n):
    images =["girl.jpg","boy.jpg","man.jpg"]
    for image in images:
        print("正在下载:",image)
        sleep(n)
        print("{}下载完成".format(image))


if __name__ == '__main__':
    t = threading.Thread(target=download, args=(1,))   #创建线程
    t.start()   #启动线程

    n = 1
    while True:
        print(n)
        sleep(1.5)
        n+=1