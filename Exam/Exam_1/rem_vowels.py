n=input("Enter a string : ")
c=""
v='aeiou'
for i in n:
    if i not in v:
        c+=i
print(c)