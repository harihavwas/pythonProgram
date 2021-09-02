lim=int(input("ENter limit : "))
lst=[]
nlst=[]
print("Enter list elements")
for i in range(lim):
    lst.append(int(input()))
print("List        : ",lst)


# method 1
n=lst[0]
while lst:
    n=lst[0]
    for j in lst:
        if j<n:
            n=j
    nlst.append(n)
    lst.remove(n)
print("Sorted List : ",nlst)


# method 2
"""
for i in range(lim):
    for j in range(i+1,lim):
        if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print("Sorted List : ",lst)
"""