"""

class Calculator:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        if self.c==1:
            self.s=self.a+self.b
        elif self.c==2:
            self.s=self.a-self.b
        elif self.c==3:
            self.s=self.a*self.b
        elif self.c==4:
            self.s=self.a/self.b
        else:
            print("Wrong Choice")
    def pr(self):
        print("Result : ",self.s)
print("1. Addition\n2. Subtration\n3. Multiplication\n4. Division")
ch=int(input("Enter your choice : "))
a=int(input("Enter 1st no. : "))
b=int(input("Enter 2nd no. : "))
ca=Calculator(a,b,ch)
ca.pr()
"""

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
print("1. Addition\n2. Subtration\n3. Multiplication\n4. Division")
ch=int(input("Enter your choice : "))
a=int(input("Enter 1st no. : "))
b=int(input("Enter 2nd no. : "))
ca=Calculator(a,b)
ca.pr()

