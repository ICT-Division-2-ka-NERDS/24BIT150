lst=[]
for i in range(1,10):
    lst.append(i)
    print("lst1",lst)
lst2=[]
for i in range(1,10,2):
    lst2.append(i)
    print("lst2",lst2)
    
lst3=[]
for i in range(2,10,2):
    if i%2==0:
        lst3.append(i)
        print("lst3",lst3)
