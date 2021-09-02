string=input("Enter string : ")
f=open('ctxt','w')
f.write(string)
f.close()
f1=open('ctxt','r')
for i in f1:
    s=i.split(" ")
dict={}
for i in s:
    if i not in dict:
        dict.update({i:1})
    else:
        v=int(dict[i])
        v+=1
        dict.update({i:v})
print(dict)
