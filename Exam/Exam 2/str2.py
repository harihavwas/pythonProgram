import re
s=input("Enter String : ")
x='[A-Z][a-z]+'
m=re.fullmatch(x,s)
if m is not None:
    print("Valid")
else:
    print("Invalid")