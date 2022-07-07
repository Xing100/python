#这是自定义进程

from multiprocessing import Process


class MYProcess(Process):

    def __init__(self,nane):
        super(MYProcess, self).__init__()    #调用父类默认方法
        self.name = nane

    def run(self):    #重写父类的run方法
        n = 1
        while True:
            print("{}-------自定义进程,n:{}".format(self.name,n))
            n += 1



if __name__ == '__main__':
    p = MYProcess("小明")
    p.start()    #启动进程
    p1 = MYProcess("小红")
    p1.start()    #启动进程