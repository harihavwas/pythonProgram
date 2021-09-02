import re
r=input("Enter Vehicle number : ")
#x='[K][L][0-9]{2}[A-Z]{1,2}[0-9]{4}'
x='[K][L]\d{2}[A-Z]{1,2}\d{4}$'
m=re.fullmatch(x,r)
if m is not None:
    print("Valid")
else:
    print("Invalid")