"""
def search(lst):
    s=int(input("Enter numbeer to search : "))
    if s in lst:
        print("Element found : ",s)
    else:
        print("Element Not found")
lim=int(input("Enter limit : "))
lst=[]
print("Enter list elements")
for i in range(lim):
    lst.append(int(input()))
search(lst)
"""



lim=int(input("Enter limit : "))
lst=[]
s=0
print("Enter list elements")
for i in range(lim):
    lst.append(int(input()))
    s=s+lst[i]
print("Sum : ",s)