"""
#que1
def prime_factors(a,d=2):
    if a<=1:
        return
    if a%d==0:
        print(d)
        prime_factors(a//d,d)
    else:
        prime_factors(a,d+1)

n=int(input("enter a number:"))
if n>0:
    print("prime factors are:")
    prime_factors(n)
else:
    print("invalid input")
#que2
def binary(a):
    if a==0:
        return
    binary(a//2)
    print(a%2,end=" ")
    


a1=int(input("enter a number gretaer than 0 :"))
binary(a1)
#que3
def stringcount(a):
    b=a.count('a')
    c=a.count('e')
    d=a.count('i')
    e=a.count('o')
    f=a.count('u')
    count=b+c+d+e+f
    print(count)
    return count
    
a1=input("enter a string:")
stringcount(a1)
#que4
def reverse_lst(a):
    lst=list(a)
    print(lst)
    lst2=lst.copy()
    lst2.reverse()
    print(lst2)
    return lst2
a1=input("enter a list:")
reverse_lst(a1)
#que5
def cal(a,b):
    c=a**b
    print(c)
    return c

a1=int(input("enter a value:"))
b1=int(input("enter a value:"))
cal(a1,b1)
#que6
def lst_value(lst):
    for i in lst:
        if (i<=0):
            lst.remove(i)
            lst.append(0)
            print(lst)
            
lst_value([1,-2,3,-4])
#que7
def avg_num(lst):
    sum=0
    for i in lst:
        sum=sum+i
        avg=sum/len(lst)
        print(avg)

avg_num([1,2,3,4,5])
#que8
def len_str(a):
    print(len(a))

a1=input("enter a string:")
len_str(a1)"""








































 
