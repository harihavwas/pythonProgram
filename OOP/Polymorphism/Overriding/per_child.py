class Person:
    def set(self,name):
        self.name=name
        print(self.name)
class Child(Person):
    def set(self,age):
        self.age=age
        print(self.age)
o=Child()
o.set("Hari")
