que=[]
s=int(input("Enter Sixe of Queue : "))
f=0
b=0
def enq():
    global f,b,s
    if b>=s:
        print("Queue is full")
    else:
        e=int(input("Enter queue element : "))
        que.append(e)
        print("Appended Successfully")
        b+=1
def deq():
    global f,b
    if f>=b+1:
        print("Empty Queue")
    else:
        que.pop(0)
        print("Removed successfully")
        f+=1
        b-=1
def display():
    print("Stack : ", que)
re=1
while(re):
    print("\nEnter your choice\n","1. Enqueue\n","2. Dequeue\n","3. Display")
    c=int(input())
    if c==1:
        enq()
    elif c==2:
        deq()
    elif c==3:
        display()
    else:
        print("Wrong choice")
    re=int(input("Do you want to continue? (0/1) : "))