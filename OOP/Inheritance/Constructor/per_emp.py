class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
class Employee(Person):
    def __init__(self,salary,dept,name,age):
        super().__init__(name,age)
        self.salary=salary
        self.dept=dept
    def print(self):
        print("Name   : ",self.name,"\nAge    : ",self.age)
        print("Salary : ",self.salary,"\ndept   : ",self.dept)
name=input("Enter your name : ")
age=int(input("Enter age : "))
salary=int(input("Enter salary : "))
dept=input("Enter Department : ")
o=Employee(salary,dept,name,age)
#o.printval()
o.print()