a=input("enter a name:")
b=input("enter a name:")
c=('arth',)
d=('yug',)
lst=[a,b,c,d]
print(lst)
count_boys=0

for e in lst:
    if isinstance(e,tuple):
        count_boys+=1

print("final_boys=",count_boys)

print("total=",len(lst))
print("girls=",len(lst)-count_boys)
