#迭代器
#通过iter()函数将可迭代的变成一个迭代器

from collections import Iterable
from collections import Iterator
a = [1,2,3]
print(isinstance(a,Iterable))   #判断列表a是否可迭代
print(isinstance(iter(a),Iterator))   #判断是否是迭代器