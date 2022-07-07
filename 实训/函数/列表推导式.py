#列表推导式    可以嵌套

a = [2,3,5,4]
#[表达式 for 变量 in 旧列表 if 表达式]
newlist = [i for i in a if i>2]
print(newlist)
#结果[3, 5, 4]

b = [[1,2,3],[1,2,5],[1,2,7],[1,2,8]]
#[表达式 for 变量 in 旧列表]
newlist1 = [i[-1] for i in b]
print(newlist1)
#结果[3, 5, 7, 8]


#[表达式 for 变量 in 旧列表]
newlist2 = [i>2 for i in a]   #newlist2 = [i+2 for i in a]
print(newlist2)
#结果[False, True, True, True]


#字典推导式
dict1 = {"Z":"z","X":"x"}
newdict1 = {value:key for key,value in dict1.items()}    #items   取出列表中的键值对
print(newdict1)