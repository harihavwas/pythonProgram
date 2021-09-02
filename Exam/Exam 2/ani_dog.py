class Animal:
    def __init__(self,name,cat):
        self.name=name
        self.cat=cat
    def printval(self):
        print("Name : ",self.name)
        print("Category : ",self.cat)
class Dog(Animal):
    def __init__(self,life,age,name,cat):
        super().__init__(name,cat)
        self.age=age
        self.life=life
    def print(self):
        print("Name : ",self.name,"\nCategory : ",self.cat)
        print("Life span : ",self.life,"\nAge : ",self.age)
name=input("Enter animal name : ")
cat=input("Enter Category : ")
life=int(input("Enter life span : "))
age=int(input("Enter age : "))
o=Dog(life,age,name,cat)
o.printval()
o.print()