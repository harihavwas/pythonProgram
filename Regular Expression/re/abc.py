import re
x='[abc]'
m=re.finditer(x,'abt c05kzabc')
for i in m:
    print(i.start())
    print(i.group())