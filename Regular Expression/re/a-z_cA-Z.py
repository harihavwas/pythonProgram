import re
x='[a-zA-Z]'
m=re.finditer(x,'abt c05AkBzabc')
for i in m:
    print(i.start(),end=" ")
    print(i.group())