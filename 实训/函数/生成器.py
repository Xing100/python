#生成器


g = (x for x in range(10))    #[] 可能是列表推导式或者元祖推导式   {}可能是集合推导式或者字典推导式   （）生成器
print(g.__next__())
print(next(g))


#在函数中出现了yield关键字，说明函数不是函数了，而是生成器     yield相当于return加暂停
#seed开始