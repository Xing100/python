import random
a = 10*100000
b = 0.0
for i in range(1,a+1):
    x,y = random.random(),random.random()
    c = pow(x*x+y*y,0.5)
    if c<=1:
        b=b+1
pi = b/a*4
print("{}".format(pi))