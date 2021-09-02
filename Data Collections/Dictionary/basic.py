"""
dict={'Name':'Hari','Age':22,'Class':'CS'}
print(dict)
print(type(dict))
print("Name  : ",dict['Name'])
print("Age   : ",dict['Age'])
print("Class : ",dict['Class'])
dict['Age']=30
print(dict)
dict['School']='SiMAT'
print(dict)
dict.update({'Loc':'PKD'})
print(dict)
del dict['Loc']
print(dict)
dict.clear()
print(dict)
del dict
print(dict)

dict={}
print(dict)
print(type(dict))
"""

"""
dict={'Name':'Hari','Age':22,'Class':'CS'}
s=input("Enter key : ")
v=input("Enter Value : ")
if s in dict.keys():
    print("Key Present")
if v in dict.values():
    print("Value Present")
"""
"""
a="hello world"
b=a.split(" ")
print(b)
for i in b:
    print(i)
"""
"""
d={1:"hello",2:{2:3,4:6}}
print(d)
"""

s=input("Enter string")
b=s.split(" ")
dict={}
for i in b:
    if i not in dict:
        dict.update({i:1})
    else:
        v=int(dict[i])
       # print(v,dict[i],)
        v+=1
        dict.update({i:v})
print(dict)
#
# KEYS ARE UNIQUE, VALUES DUPLICATION ALLOWED
# KEYS SAME Type
# MUTABLE
# KEYS HOMO
# VAL HETRO
# NESTING POSSIBLE