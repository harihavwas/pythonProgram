import re
s=input("Enter email : ")
x='[a-zA-Z0-9]+[@][a-z][.][a-z]{2,3}'
m=re.fullmatch(x,s)
if m is not None:
    print("Valid")
else:
    print("Invalid")