import re
s=input("Enter String : ")
x='^[A-Z]\w{3,8}[A-Z]$'
m=re.fullmatch(x,s)
if m is not None:
    print("Valid")
else:
    print("Invalid")