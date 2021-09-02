import re
f=open('phn','r')
x='[+][9][1]\d{10}$'
for i in f:
    s=i.rstrip('\n')
    m=re.fullmatch(x,s)
    if m!=None:
        print(s)