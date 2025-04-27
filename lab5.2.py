import random
lst=[]
for i in range(20):
    num=random.randint(1,100)
    lst.append(num)
    print("list:",lst)

n=int(input("enter a number :"))
print("positions:")
for i in range(20):
    if lst[i]==n:
        print(i)
    else:
        print("not present")

