"""

Set features
1. Not keeping order
2. Not support duplicate elements
3. Hetrogenous
4. Mutable
5. Nesting not possible


"""













# 1. Inputing from keyboard
"""
l=int(input("Enter Set limit : "))
a=set()
print("Enter Elements")
for i in range (l):
    a.add(int(input()))
print(a)
print(type(a))
"""



# 2. Square set
"""
b=set()
a={1,2,3,4,5,6,7,8,9}
for i in a:
    b.add(i**2)
print(b)
"""


# 3. Odd or Even Set
"""
b=set()
c=set()
a={1,2,3,4,5,6,7,8,9,12,33,44,55,78,39,44}
for i in a:
    if i%2==0:
        b.add(i)
    else:
        c.add(i)
print("Set      : ",a)
print("Even Set : ",b)
print("Odd Set  : ",c)
"""


# 4. Common Elements
"""
s1={1,2,3,4,5,6,7}
s2={5,6,7,8,9,10}
print("Common Elemets : ")
for i in s1:
    if i in s2:
        print(i)
print("Total Elements  : ",s1.union(s2))
print("Common Elements : ",s1.intersection(s2))
print("Difference      : ",s1.difference(s2))
"""

s=set()
p=set()
np=set()
lim=int(input("Enter limit : "))
print("Enter values")
for i in range(lim):
    s.add(int(input()))
for i in s:
   c=0
   for j in range(2,i):
       if (i%j==0):
           c+=1
   if c==0:
       p.add(i)
   else:
       np.add(i)
print("Set           : ",s)
print("Prime Set     : ",p)
print("Non-prime set : ",np)