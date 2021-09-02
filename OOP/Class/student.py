"""
class Student:
    def setval(self,name,roll,sch):
        self.name=name
        self.roll=roll
        self.sch=sch
    def printval(self):
        print("Name : ",self.name)
        print("Roll No.  : ",self.roll)
        print("School : ",self.sch)
p1=Student()
name=input("Enter Name : ")
roll=int(input("Enter Roll No. : "))
sch=input("Enter School Name : ")
p1.setval(name,roll,sch)
p1.printval()
"""

class Student:
    school="simat"
    def setval(self,name,roll,sch):
        self.name=name
        self.roll=roll
        self.sch=sch
    def printval(self):
        print("Name : ",self.name)
        print("Roll No.  : ",self.roll)
        print("School : ",self.sch)
        print(Student.school)
p1=Student()
name=input("Enter Name : ")
roll=int(input("Enter Roll No. : "))
sch=input("Enter School Name : ")
p1.setval(name,roll,sch)
p1.printval()