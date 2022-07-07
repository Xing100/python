from 实训 import 时间

scale = 50
print("执行开始".center(scale//2,"-"))
start = 时间.perf_counter()
for i in range(scale+1):
    a = '*'*i
    b = '.'*(scale-i)
    c = (i/scale)*100
    dur = 时间.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    时间.sleep(0.1)
print("\n"+"执行结束".center(scale // 2, "-"))
