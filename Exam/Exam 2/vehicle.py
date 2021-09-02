class Vehicle:
    def set(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color
class Bus(Vehicle):
    def show(self):
        print("Model : ",self.model)
        print("Reg no : ",self.regno)
        print("Color : ",self.color)
model=input("Enter Vehicle Model : ")
regno=input("Enter Register Number : ")
color=input("Enter Color : ")
v=Bus()
v.set(model,regno,color)
v.show()