#que1
"""def fun():
    a=print("hello")
    return a

def disp():
    b=print("hi")
    return b
def msg():
    c=print("bye")
    return c
lst=[fun,disp,msg]
list(map(lambda f:f(),lst))"""
#que2


"""lst1=[1,2,3,4,5,6]
lst2=[6,5,4,3,2,1]
lst3=list(map(lambda x,y:x+y,lst1,lst2))
print(lst3)
#que3
import random
lst=[]
for i in range(10):
    num=random.randint(-15,15)
    lst.append(num)
    print(lst)
lst2=list(map(lambda x:x**2,lst))
print(lst2)

#que4
lst=['madam','python','malyalam',12321]
lst2=list(filter(lambda x: str(x)==str(x)[::-1],lst))
print(lst2)

#que5
lst=['vishwap','heer','arth','yug','dhwiti','anonymous']
lst2=list(filter(lambda x: len(x)<8,lst))
print(lst2)
"""
