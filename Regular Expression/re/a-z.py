import re
x='[a-z]'
m=re.finditer(x,'abt c05kzabc')
for i in m:
    print(i.start())
    print(i.group())