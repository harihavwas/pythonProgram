import re
f=open('phn','r')
f1=open("nph","w")
x='[+][9][1]\d{10}$'
for i in f:
    s=i.rstrip('\n')
    m=re.fullmatch(x,s)
    if m!=None:
        f1.write(s+"\n")
        #print(s)
f1.close()
f2=open("nph","r")
for k in f2:
    print(k)