import random
lst=[]
for i in range(50):
    num=random.randint(1,30)
    lst.append(num)
    print(lst)
lst2=set(lst)
print(lst2)
lst3=list(lst2)
print(lst3)
