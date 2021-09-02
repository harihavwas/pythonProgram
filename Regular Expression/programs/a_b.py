import re
s=input("Enter string : ")
x='^a[a-zA-Z0-9\W]*b$'
m=re.fullmatch(x,s)
if m is not None:
    print("Valid")
else:
    print("Invalid")