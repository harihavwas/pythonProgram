
class Employee:
    cmpname=input("Enter Company Name : ")
    def __init__(self,ide,name,age,salary,dept):
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

name=input("Enter Name : ")
age=int(input("Enter Age : "))
ide=int(input("Enter ID : "))
salary=int(input("Enter salary : "))

dept=input("Enter Department : ")
p1=Employee(ide,name,age,salary,dept)
p1.printval()