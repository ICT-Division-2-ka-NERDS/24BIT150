import random
odd=[]
even=[]
for i in range(5):
    num=random.randrange(1,100,2)
    odd.append(num)

    print(odd)
for i in range(4):
    num=random.randrange(2,100,2)
    even.append(num)
    print(even)

odd.insert(2,even)
print(odd)
