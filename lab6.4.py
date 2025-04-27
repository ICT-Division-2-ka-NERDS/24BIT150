import operator
lst=[('b',100),('a',200),('c',300)]
lst=sorted(lst,key=operator.itemgetter(1),reverse=True)
print(lst)
