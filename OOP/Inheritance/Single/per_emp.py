
"""#  Single Inheritance
class Person:
    def setv(self,name,ide,dept,salary):
        self.name=name
        self.ide = ide
        self.dept = dept
        self.salary=salary
class Employee(Person):
    def exam(self):
        print("Name : ",self.name)
        print("ID   : ",self.ide)
        print("Salary : ",self.salary)
        print("Department : ",self.dept)
name=input("Enter Name : ")
ide=int(input("Enter ID : "))
salary=int(input("Enter salary : "))
dept=input("Enter Departmet : ")




pe=Person()
pe.setv(name,ide,dept,salary)

st=Employee()

st.setv(name,ide,dept,salary)
st.exam()

"""



class Person:
    def set(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add
        print("Name : ",self.name,"\nAge : ",self.age,"\nAddress : ",self.add)
class Employee(Person):
    def setval(self,ide,salary,dept):
        self.ide=ide
        self.salary=salary
        self.dept=dept
        print("\nID : ",self.ide,"\nSalary : ",self.salary,"\nDepartment : ",self.dept)
name=input("Enter Name : ")
age=int(input("Enter Age : "))
add=input("Enter address :")
ide=int(input("Enter ID : "))
salary=int(input("Enter Salary : "))
dept=input("Enter Department : ")
e=Employee()
e.set(name,age,add)
e.setval(ide,salary,dept)