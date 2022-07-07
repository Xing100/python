list1 = [{"a":5,"b":6},{"a":8,"b":6},{"a":3,"b":6},{"a":9,"b":6}]

c = max(list1,key=lambda x:x["a"])
print(c)



print("----------------map()函数")
#map(func, *iterables)    函数   可迭代对象    对列表进行累加
list2 = [1,2,3]
d = map(lambda x:x+1,list2)
print(d)
print(list(d))



print("----------------reduce()函数")
from functools import reduce
#reduce(function, sequence(序列)[, initial])    initial加一个初始值    求和
list3 = [1,2,3,4]
r = reduce(lambda x,y:x+y,list3,2)
print(r)



print("----------------filter()函数")
# filter(function or None, iterable)    筛选
list4 = [10,12,5,15,18,6]
z = filter(lambda x:x>10,list4)
print(z)
print(list(z))



print("----------------sorted()函数")
#sorted(iterable,key,reverse)    排序  True  降序   False   升序
list5 = [{"a":1},{"a":3},{"a":5},{"a":7}]
x = sorted(list5,key=lambda x:x["a"],reverse = True)
print(list(x))