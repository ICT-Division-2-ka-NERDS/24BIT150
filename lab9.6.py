def create_list(a):
    lst=[]
    for x in range(1,a+1):
        lst.append((x,x**2,x**3))
        print(lst)
    return lst



a1=int(input("enter a value:"))
create_list(a1)
