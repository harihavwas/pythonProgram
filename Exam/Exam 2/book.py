class Book:
    def set(self,name):
        self.name=name
        print(self.name)
class Child(Book):
    def set(self,price):
        self.price=price
        print(self.price)
o=Child()
book=input("Enter Book name: ")
price=int(input("Enter Price : "))
o.set(book)
o.set(price)