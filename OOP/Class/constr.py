# initialize instance variables

class Const:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def pri(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
c1=Const("Hari",22)
c1.pri()