import re
f=open('lumlist','r')
x='[LUM]{3}[0-9]{2}[PY]{2}[0-9]{3}'
f1=open('lumfnlist','w')
for i in f:
    s=i.rstrip('\n')
    m=re.fullmatch(x,s)
    if m!=None:
        print(s)
        f1.write(s+"\n")
