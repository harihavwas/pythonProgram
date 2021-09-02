import re
s=input("Enter string : ")
x='\D{8,15}'
m=re.fullmatch(x,s)
if m is not None:
    print("Valid")
else:
    print("Invalid")