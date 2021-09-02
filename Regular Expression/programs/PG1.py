# COMBINATION OF UPPERCASE AND LOWERCASE ENDING WITH A NUMBER
import re
s=input("Enter String : ")
x='[a-zA-Z]+\d'
m=re.fullmatch(x,s)
if m is not None:
    print("Valid")
else:
    print("Not valid")