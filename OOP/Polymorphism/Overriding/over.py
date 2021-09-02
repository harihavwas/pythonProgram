class Parent:
    def showa(self,con):
        self.con=con
        print(self.con)
class Child(Parent):
    def show(self,name):
        self.name=name
        print(self.name)
o=Child()
o.show("811")