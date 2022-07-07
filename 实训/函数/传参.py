#传参过程   1赋值给n   n又赋值给a
def decorate(fun):
    a = 100
    def wrapper(n):    #一个参数  变量   多个参数 *变量    关键字参数  **变量
        fun(n)     #一个参数  变量   多个参数 *变量    关键字参数  **变量
        print("刷漆")
        print("铺地板",a)
    return wrapper       #返回的是内存地址

@decorate
def house(a):   #带有参数
    print("毛坯房",a)
"""
1.house是被装饰函数。
2.将被装饰函数作为参数转给装饰器decorate
3.执行decorate函数
4.将返回值又赋值给house
"""
house(1)  #传参