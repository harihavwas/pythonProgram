import re
x='[0-9]'
m=re.finditer(x,'abt c05AkBzabc')
for i in m:
    print(i.start(),end=" ")
    print(i.group())