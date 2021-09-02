def mult(lst,l):
    s=1
    for i in lst:
        s=s*i
    print("Multiplied Result : ",s)
l=int(input("Enter limit : "))
lst=[]
print('Enter list elements')
for i in range(l):
    lst.append(int(input()))
print("List : ",lst)
mult(lst,l)

