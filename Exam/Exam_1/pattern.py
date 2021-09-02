"""
k=1
for s in range(2):
    for i in range(6):
        for j in range(i):
            print(k,end=" ")
        print("")
    k+=1
    for i in range(6,0,-1):
        for j in range(0,i-1):
            print(k,end=" ")
        print("")
    k+=1
    """

a=int(input("Enter Initial range : "))
b=int(input("Enter Final range : "))
for i in range(a,b):
    if (i%2==0):
        for k in range(r,0,-1):
            for j in range(0,k):
                print(i,end=" ")
            print("\r")
    else:
        for l in range(b):
            for m in range(0,l+1):
                print(i,end=" ")
            print("\r")