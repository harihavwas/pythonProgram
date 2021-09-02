class Add:
    def addition(self,a,b):
        self.c=a+b
    def printing(self):
        print("Result : ",self.c)
a=Add()
n1=int(input("Enter 1st number : "))
n2=int(input("Enter 2nd number : "))
a.addition(n1,n2)
a.printing()