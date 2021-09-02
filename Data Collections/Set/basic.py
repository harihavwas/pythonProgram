a={0,1,2,3}
print(a)
print(type(a))



b=set()
print(b)
print(type(b))
b.add(2)
b.add(4)
print(b)


c={8,4,6}
c.add(True)
c.add(False)
c.add(4.5)
print(c)
print(type(c))

d={0,9,7,2,5,9}
d.add('hello')
for i in range(4):
    d.add(input())
print(d)
print(type(d))
