# minimum and maximum
import re
x='a{1,4}'
r='aaa abc aaaaaaa cga'
m=re.finditer(x,r)
for i in m:
    print(i.start(),end=" ")
    print(i.group())

"""
0 aaa
4 a
8 aaaa
12 aaa
18 a
"""