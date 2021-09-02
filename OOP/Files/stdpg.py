class Student:
    def __init__(self,name,roll,cor,mark):
        self.name=name
        self.roll=roll
        self.cor=cor
        self.mark=mark
    def printv(self):
        print(self.name, self.roll,self.cor,self.mark)
string=input("Enter Name, roll, corse, mark")
f=open('newstd','w')
f.write(string)
f.close()
f1=open('newstd','r')
for i in f1:
    r=i.split(",")
    o = Student(r[0],r[1],r[2],r[3])
    o.printv()

