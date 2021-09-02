class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printv(self):
        print(self.name, self.age)

f1=open('student','r')
for i in f1:
    r=i.split(",")
    o = Student(r[0],r[1])
    o.printv()

