class Person:
    def set(self,name,age):
        self.name=name
        self.age=age
        print("Name: ",self.name,"\nAge : ",self.age)
class Child:
    def setv(self,sch,std):
        self.sch=sch
        self.std=std
        print("School : ",self.sch,"\nStandard : ",self.std)
class Student(Person,Child):
    def pri(self,mark,roll):
        self.mark=mark
        self.roll=roll
        print("\nMark : ",self.mark,"\nRoll No: ",self.roll)
name=input("Enter name : ")
age=int(input("Enter age: "))
sch=input("Enter School : ")
std=int(input("Enter Standard : "))
roll=int(input("Enter roll no : "))
mark=int(input("Enter Mark : "))
s=Student()
s.set(name,age)
s.setv(sch,std)
s.pri(mark,roll)