class Person:
    def set1(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add
        print("Name : ",self.name,"\nAge : ",self.age,"\nAddress : ",self.add)
class Parent:
    def set2(self,pname,cnt):
        self.pname=pname
        self.cnt=cnt
        print("\nGuardian Name : ",self.pname,"\nContact : ",self.cnt)
class Employee(Person,Parent):
    def set3(self,salary,dept):
        self.salary=salary
        self.dept=dept
        print("\nSalary :",self.salary,"\nDepartment : ",self.dept)

name=input("Enter name:  ")
age=int(input("Enter Age : "))
add=input("Enter Address : ")
pname=input("Enter gaurdian name : ")
cnt=int(input("Enter Contact : "))
salary=int(input("ENter Salary : "))
dept=input("Enter Department : ")
o=Employee()
o.set1(name,age,add)
o.set2(pname,cnt)
o.set3(salary,dept)
