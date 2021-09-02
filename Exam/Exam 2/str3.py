import re
s=input("Enter String : ")
x='^a\d+b$'
m=re.fullmatch(x,s)
if m is not None:
    print("Valid")
else:
    print("Invalid")