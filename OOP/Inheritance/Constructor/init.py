class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
class Student(Person):
    def __init__(self,roll,mark,name,age):
        super().__init__(name,age)
        self.roll=roll
        self.mark=mark
    def print(self):
        print("Name    : ",self.name,"\nAge     : ",self.age)
        print("Roll no : ",self.roll,"\nMark    : ",self.mark)
o=Student(2,34,"Hari",22)
#o.printval()
o.print()