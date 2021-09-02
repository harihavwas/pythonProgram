import re
s=input("Enter String : ")
x='[0-9]'
m=re.finditer(x,s)
if m is not None:
    print("Valid")
else:
    print("Invalid")