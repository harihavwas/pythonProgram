class Person:
    def per(self,name):
        self.name=name
        print("Name : ",self.name)
class Parent:
    def par(self,pname,pcnt):
        self.pname=pname
        self.pcnt=pcnt
        print("Parent Name : ",self.pname,"\nParent Contact : ",self.pcnt)
class Child(Person,Parent):
    def child(self,age):
        self.age=age
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
pname=input("Enter Parent Name : ")
pcnt=int(input("ENter Parent Contact : "))

p=Person()
c=Child()
s=Student()
pa=Parent()

p.per(name)

c.child(age)
c.per(name)
c.par(pname,pcnt)

pa.par(pname,pcnt)

s.std(clas,sch)
s.child(age)
s.per(name)
