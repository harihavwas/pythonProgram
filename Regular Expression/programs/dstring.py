import re
r='56kg'
x='[0-9]{2}[k][g]'
m=re.fullmatch(x,r)
if m is not None:
    print("Valid")
else:
    print("Invalid")
