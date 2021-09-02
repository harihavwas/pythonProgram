def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def fdiv(n1,n2):
    return n1//n2
def exp(n1,n2):
    return n1**n2
while(True):
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Floor division\n6. Exponent")
    ch=int(input("Enter your choice : "))
    n1=int(input("Enter number : "))
    n2=int(input("Enter another number : "))
    if ch==1:
        r=add(n1,n2)
        print(n1," + ",n2," = ",r)
    elif ch==2:
        r=sub(n1,n2)
        print(n1," - ",n2," = ",r)
    elif ch==3:
        r=mul(n1,n2)
        print(n1," x ",n2," = ",r)
    elif ch==4:
        r=div(n1,n2)
        print(n1," / ",n2," = ",r)
    elif ch==5:
        r=fdiv(n1,n2)
        print(n1," // ",n2," = ",r)
    elif ch==6:
        r=exp(n1,n2)
        print(n1," ^ ",n2," = ",r)
    else:
        print("Wrong Choice\n")
        exit()
