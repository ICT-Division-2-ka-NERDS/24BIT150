queue=[]
while True:
    print("queue menu ")
    print("enqueue ")
    print("dequeue ")
    print("display queue")
    print("exit ")

    n=input("enter a number :")
    if n=='1':
        a=input("enter a number ;")
        queue.append(a)
        print("item added to queue")
    elif n=='2':
        if not queue:
            print("queue is empty")
        else:
            remove=queue.pop(0)
            print(remove)
    elif n=='3':
        if not queue:
            print("queue is empty")

        else:
            print(queue)
    elif n=='4':
        print("exit program")
        break
    else:
        print("invalid")
