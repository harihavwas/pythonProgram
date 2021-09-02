# considering 2 a with their indices
import re
x='a{2}'
r='aaa abc aaaa cga'
m=re.finditer(x,r)
for i in m:
    print(i.start(),end=" ")
    print(i.group())