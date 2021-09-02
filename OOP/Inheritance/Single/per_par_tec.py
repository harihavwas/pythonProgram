class Person:
    def set1(self,name,age,add):
        self.name=name
        self.age=age
        self.add=add
        print("Name : ",self.name,"\nAge : ",self.age,"\nAdress : ",self.add)
class Parent:
    def set2(self,rname,rcnt,rel):
        self.rname=rname
        self.rcnt=rcnt
        self.rel=rel
        print("Parent name : ",self.rname,"\nParent Contact : ",self.rcnt,"\nParent Relation : ",self.rel)
class Teacher(Person,Parent):
    def set3(self,tname,tcnt,tmail):
        self.tname=tname
        self.tcnt=tcnt
        self.tmail=tmail
        print("Teacher name : ",self.tname,"\nTeacher contact : ",self.tcnt,"\nTeacher Mail : ",self.tmail)
name=input("Enter Name : ")
age=int(input("Enter Age : "))
add=input("Enter Address : ")
rname=input("Enter Parent name : ")
rcnt=int(input("Enter Parent Contact : "))
rel=input("Enter relation to the parent : ")
tname=input("Enter Teacher name : ")
tcnt=int(input("Enter Teacher Contact : "))
tmail=input("Enter Teacher Mail ID : ")
o=Teacher()
o.set1(name,age,add)
o.set2(rname,rcnt,rel)
o.set3(tname,tcnt,tmail)