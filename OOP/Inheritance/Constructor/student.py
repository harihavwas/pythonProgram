class Student:
    def __init__(self,name,roll,dept,clg):
        self.name=name
        self.roll=roll
        self.dept=dept
        self.clg=clg
    def printv(self):
        print("Name : ",self.name,"\nRoll : ",self.roll,"\nDepartment : ",self.dept,"College : ",self.clg)
    def __str__(self):
        return self.name+str(self.roll)

name=input("Enter Name : ")
roll=int(input("Enter Roll : "))
dept=input("Enter Department : ")
clg=input("Enter College : ")
o=Student(name,roll,dept,clg)
o.printv()
print(o)