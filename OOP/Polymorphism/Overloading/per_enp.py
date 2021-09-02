class Person:
    def set(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Employee(Person):
    def set(self,dept):
        self.dept=dept
        print(self.dept)
o=Employee()
o.set("Hari")