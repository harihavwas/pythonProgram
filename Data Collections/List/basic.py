"""
1. Hetrogenous
2. Keeps order
3. Support duplicate elements
"""

"""
lst=[1,2,3,4,5,6]
print(lst)
print(type(lst))
for i in lst:
    print(i)
lst2=[1,'Hello',True,8.6]
print(lst2)
lst2.append(98)
print(lst2)
"""
"""
l=int(input("Enter limit : "))
lst=[]
print("Enter list elements")
for i in range(l):
    lst.append(int(input()))
print("List : ",lst)
"""


# NESTING, remove, clear, delete
"""
lst=[1,2,3,[4,5,6,[7,8,9]]]
lst.remove(2)
lst.clear()
del lst
print(lst)
"""


# SQARE OF LIST
"""
lim=int(input("Enter limit : "))
lst1=[]
lst2=[]
print("Enter List elements")
for i in range(lim):
    lst1.append(int(input()))
print("List         : ",lst1)
for i in range(lim):
    lst2.append(lst1[i]**2)
print("Squared List : ",lst2)
"""

# UPDATE
"""
lst=[1,2,3,4,5,6]
print(lst)
lst[0]=99
print(lst)
"""

# APPEND AND EXTEND
lst=['abc','def']
nlst=[0,1,2,3,4]
print(lst,"\n",nlst)
nlst.extend(lst)
print(nlst)