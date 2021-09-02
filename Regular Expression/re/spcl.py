import re
x='[^0-9a-zA-Z]'
m=re.finditer(x,'abt9 c@5kAz')
for i in m:
    print(i.start(),end=" ")
    print(i.group())