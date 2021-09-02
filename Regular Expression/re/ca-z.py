import re
x='[A-Z]'
m=re.finditer(x,'abt cA05kzabc')
for i in m:
    print(i.start())
    print(i.group())