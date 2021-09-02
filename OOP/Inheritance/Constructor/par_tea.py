class Parent:
    def __init__(self,name):
        self.name=name
class Teacher(Parent):
    def __init__(self,name,email):
        super().__init__(name)
        self.email=email
    def printv(self):
        print("Name : ",self.name,"\nEmail : ",self.email)
    def __str__(self):
        return str(self.name)
name=input("Enter Name : ")
email=input("Enter Email : ")
o=Teacher(name,email)
o.printv()
print(o)