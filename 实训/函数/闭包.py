#函数闭包
#1.外部函数中定义了内部函数
#2.外部函数是有返回值
#3.返回值是：内部函数名
#4.内部函数引用了外部函数的变量


def waiceng():
    a = 10
    def neiceng():
        print("我是内层函数！！")
        print(a)
    return neiceng     #返回的是内存地址

b = waiceng()  #把外层函数的返回值赋值给b   b现在是内层函数
b()
