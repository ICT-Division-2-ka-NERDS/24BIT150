stack=[]
while True:
    print("stack menu")
    print("push ")
    print("pop")
    print("display")
    print("exit")

    n=input("enter a number 1-4:")
    if n=='1':
        a=input("enter a num:")
        stack.append(a)
        print("item pushed",stack)
    elif n=='2':
        if not stack:
            print("stack is empty")
        else:
            popped=stack.pop()
            print("popped item",popped)
    elif n=='3':
        if not stack:
            print("stack is empty")
        else:
            print("stack content",stack)
    elif n=='4':
        print("exit program")
        break
    else:
        print("invalid choice ")
