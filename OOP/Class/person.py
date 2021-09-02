class Person:
    def setval(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("Name : ",self.name)
        print("Age  : ",self.age)
p1=Person()
name=input("Enter Name : ")
age=int(input("Enter Age : "))
p1.setval(name,age)
p1.printval()