#que6
a=float(input("enter a number:"))
b=float(input("enter a number:"))
c=float(input("enter a number:"))
temp=[a,b,c]#fahrenheit 
print(temp)
cel=[]
for i in temp:
    c=(i-32)*5/9
    cel.append(c)
    print(cel)
