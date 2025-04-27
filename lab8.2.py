set1=set()
count=0
import random
for i in range(10):
    num=random.randint(15,45)
    set1.add(num)
    print(set1)

    if num<30:
        count+=1
        print(count)
        print(set1)

    if num>35:
        set1.remove(num)
        print(set1)
    
