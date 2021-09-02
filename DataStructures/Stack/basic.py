"""
1. Stack
    --> LIFO
    --> Push : Add element
    --> Pop : Remove element
    --> Display
    --> Size
"""
lst=[]
s=int(input("Enter size : "))
t=0
def push():
    global t,s
    if t>=s:
        print("Stack is full")
    else:
        n=int(input("Enter element : "))
        lst.append(n)
        print("Appended successfully")
        t+=1
def pop():
    global t
    if t<=0:
        print("Stack is empty. Cannot Delete Element")
    else:
        lst.pop()
        print("Removed successfully")
        t-=1
def display():
    print("Stack : ",lst)
re=1
while(re):
    print("Enter your choice\n","1. Push\n","2. Pop\n","3. Display\n")
    c=int(input())
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        display()
    else:
        print("Wrong choice")
    re=int(input("Do you want to continue? (0/1) : "))