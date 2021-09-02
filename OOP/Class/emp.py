"""
class Employee:
    def setval(self,ide,name,age,salary,cmpname,dept):
        self.name=name
        self.age=age
        self.ide=ide
        self.salary=salary
        self.cmpname=cmpname
        self.dept=dept
    def printval(self):
        print("ID         : ",self.ide)
        print("Name       : ",self.name)
        print("Age        : ",self.age)
        print("Salary     : ",self.salary)
        print("Company    : ",self.cmpname)
        print("Department : ",self.dept)
p1=Employee()
name=input("Enter Name : ")
age=int(input("Enter Age : "))
ide=int(input("Enter ID : "))
salary=int(input("Enter salary : "))
cmpname=input("Enter Company Name : ")
dept=input("Enter Department : ")
p1.setval(ide,name,age,salary,cmpname,dept)
p1.printval()
"""

class Employee:
    cmpname=input("Enter Company Name : ")
    def setval(self,ide,name,age,salary,dept):
        self.name=name
        self.age=age
        self.ide=ide
        self.salary=salary

        self.dept=dept
    def printval(self):
        print("ID           : ",self.ide)
        print("Name         : ",self.name)
        print("Age          : ",self.age)
        print("Salary       : ",self.salary)

        print("Department   : ",self.dept)
        print("Company Name : ",Employee.cmpname)
p1=Employee()
name=input("Enter Name : ")
age=int(input("Enter Age : "))
ide=int(input("Enter ID : "))
salary=int(input("Enter salary : "))

dept=input("Enter Department : ")
p1.setval(ide,name,age,salary,dept)
p1.printval()