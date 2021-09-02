class Vehicle:
    def __init__(self,model,reg,color):
        self.model=model
        self.reg=reg
        self.color=color
    def printv(self):
        print("Model : ",self.model,"\nRegister No : ",self.reg,"\nColor : ",self.color)
    def __str__(self):
        return self.model
model=input("Enter Model : ")
reg=input("Enter Register no : ")
color=input("Enter color : ")
o=Vehicle(model,reg,color)
o.printv()
print(o)