

#定义装饰器
def canshu(c):
    def decorate(fun):   #fun获得house函数的内存地址
        a = 100
        def wrapper():   #闭包
            fun()    #调用的实际是house()函数
            print("刷漆",a)
            print("铺地板",c)
        return wrapper      #返回的是内存地址
    return decorate       #返回的是内存地址
#使用装饰器
@canshu(2)
def house():
    print("毛坯房")

house()

