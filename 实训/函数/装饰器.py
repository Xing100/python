#1.函数作为参数传递
#2.要有闭包的特点

#定义装饰器
def decorate(fun):   #fun获得house函数的内存地址
    a = 100
    def wrapper():   #闭包
        fun()    #调用的实际是house()函数
        print("刷漆")
        print("铺地板",a)
    return wrapper       #返回的是内存地址
#使用装饰器
@decorate
def house():
    print("毛坯房")
"""
1.house是被装饰函数。
2.将被装饰函数作为参数转给装饰器decorate
3.执行decorate函数
4.将返回值又赋值给house
"""
house()    #调用的实际是wrapper()函数
# 输出house   print(house) 得到是装饰器wrapper的内存地址  <function decorate.<locals>.wrapper at 0x0000023B0EB3D268>

