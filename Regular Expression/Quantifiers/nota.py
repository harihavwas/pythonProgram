# check strating with a
import re
x='^a'
r='aaa abc aaaaaaa cga'
m=re.finditer(x,r)
for i in m:
    print(i.start(),end=" ")
    print(i.group())
