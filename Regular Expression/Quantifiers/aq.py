# considering all position with a 
import re
x='a?'
r='aaa abc aaaa cga'
m=re.finditer(x,r)
for i in m:
    print(i.start(),end=" ")
    print(i.group())