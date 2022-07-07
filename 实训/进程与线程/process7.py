#Queue

from multiprocessing import Queue

q = Queue(3)     #创建队列个数
q.put("A")     #将A添加到队列     put(self, obj, block=True, timeout=None)   block=Ture 阻塞   timeout设置超时时间  默认没有超时时间
q.put("B")
q.put("C")
print(q.get())      #得到队列    get(self, block=True, timeout=None)   block=Ture 阻塞   timeout设置超时时间  默认没有超时时间
print(q.full())     #判断队列是否满了
print(q.empty())    #判断队列是否为空
