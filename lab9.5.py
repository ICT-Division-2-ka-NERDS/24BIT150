def ispangram(a):
    set1=set(a)
    aset=set("abcdefghijklmnopqrstuvwxyz")
    print(set1)
    if (aset.issubset(set1)==True):
        print("pangram")
    else:
        print("not pangram")
    return set1


a1=input("enter a string:")
ispangram(a1)
