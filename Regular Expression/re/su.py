import re
s=input("Enter string : ")
x='(^[A-Z][a-z0-9\W]*)'
m=re.fullmatch(x,s)
if m is not None:
    print("Valid")
else:
    print("Invalid")