fullset={"Arth","Apple",'Banana','Ball'}
set1=set()
set2=set()

lst=list(fullset)
print(lst)
for i in fullset:
    if i.startswith("A"):
        set1.add(i)
        print(set1)

    elif i.startswith("B"):
        set2.add(i)
        print(set2)
