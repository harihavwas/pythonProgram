"""
import re
r=input("Enter phn no : ")
x='\d{10}'
m=re.fullmatch(x,r)
if m is not None:
    print("Valid")
else:
    print("Invalid")
"""

import re
r=input("Enter phn no : ")
x='[+91]{3}[0-9]{10}'
m=re.fullmatch(x,r)
if m is not None:
    print("Valid")
else:
    print("Invalid")