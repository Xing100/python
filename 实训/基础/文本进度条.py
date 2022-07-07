from 实训 import 时间

z = 10
print("------执行开始------")
for i in range(z+1):
    a = i*'*'
    b = '.'*(10-i)
    c = (i/z)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    时间.sleep(5)
print("------执行结束------")