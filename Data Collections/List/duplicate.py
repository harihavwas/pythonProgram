# DUPLICATE ELEMENT
def dup(lst):
    b=[]
    for i in lst:
        if i not in b:
            b.append(i)
        else:
            print(i)
l=int(input("ENter limit : "))
lst=[]
print('Enter list elements')
for i in range(l):
    lst.append(int(input()))
dup(lst)