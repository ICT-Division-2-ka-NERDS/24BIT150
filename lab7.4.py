a=input("enter a string:")
lst=list(a)
print(lst)
for i in lst:
    a=lst.count(i)
    dict={i:a}
    print(dict)
