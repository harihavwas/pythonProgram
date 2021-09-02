import re
c=0
m=re.finditer('ab','abaabbab')
print(m)
for i in m:
    c+=1
print(c)