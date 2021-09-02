def oddeven(lst,l):
    elst=[i for i in lst if i%2==0]
    olst=[i for i in lst if i%2!=0]
    """
    for i in lst:
        if i%2==0:
            elst.append(i)
        else:
            olst.append(i)
            """
    print('Even List : ',elst,"\nOdd List  : ",olst)

l=int(input("Enter limit : "))
lst=[]
print('Enter list elements')
for i in range(l):
    lst.append(int(input()))
print("List      : ",lst)
oddeven(lst,l)
