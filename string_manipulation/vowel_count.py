n=input("Enter a string")
v="aeiou"
c=0
for i in n:
    if i in v:
        c=c+1
print(c)