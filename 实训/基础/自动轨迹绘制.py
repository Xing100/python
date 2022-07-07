import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600)
t.pencolor("red")
t.pensize(5)
date=[]
f = open("f.txt")
for l in f:
    l = l.replace("\n","")
    date.append(list(map(eval,l.split(","))))
for i in range(len(date)):
    t.pencolor(date[i][3],date[i][4],date[i][5])
    t.fd(date[i][0])
    if date[i][1]:
        t.right(date[i][2])
    else:
        t.left(date[i][2])
t.done()

