class Person:
    def per(self,name):
        self.name=name
class Child(Person):
    def child(self,age):
        self.age=age
        print("Name : ", self.name)
        print("Age : ",self.age)
class Student(Child):
    def std(self,clas,sch):
        self.clas=clas
        self.sch=sch
        print("Class : ",self.clas,"\nSchool : ",self.sch)
name=input("Enter Name : ")
age=int(input("Enter Age : "))
clas=int(input("Enter Class : "))
sch=input("Enter School : ")
p=Person()
p.per(name)
c=Child()
c.child(age)
c.per(name)
s=Student()
s.std(clas,sch)
s.child(age)
s.per(name)