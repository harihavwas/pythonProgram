class Student:
    def __init__(self,name,id,course,mark):
        self.name=name
        self.id=id
        self.course=course
        self.mark=mark
    def printt(self):
        print("Name: ",self.name)
        print("Id : ",self.id)
        print("Course : ",self.course)
        print("Mark : ",self.mark)
'''
open('mlist','r')
c=0
for i in f:
    s=i.rstrip("\n").split(",")
    if int(s[3])>c:
        c=int(s[3])
        ls=s
o=Student(ls[0],ls[1],ls[2],ls[3])
o.print()
'''
lst=[]
f=open("mlist","r")
for i in f:
    d=i.rstrip("\n").split(",")
    #print(d)
    name=d[0]
    id=d[1]
    course=d[2]
    mark=d[3]
    s=Student(name,id,course,mark)
    s.printt()
    lst.append(s)
#print(lst)
mark=[]
for st in lst:
    mark.append(st.mark)
print(mark)
for st in lst:
    if (st.mark==max(mark)):
        print(st.id,st.name,st.course,st.mark)