class Person:
    def show(self,name):
        self.name=name
        print(self.name)
class Student(Person):
    def show(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
        print(self.name,self.roll,self.age)
o=Student()
o.show("Hari")