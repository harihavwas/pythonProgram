class Teacher:
    clgname=input("Enter College Name : ")
    def __init__(self,ide,name,sub,dept):
        self.name=name
        self.sub=sub
        self.dept=dept
        self.ide=ide

        self.dept=dept
    def printval(self):
        print("ID           : ",self.ide)
        print("Name         : ",self.name)
        print("Subject      : ",self.sub)
        print("Department   : ",self.dept)
        print("Company Name : ",Teacher.clgname)

name=input("Enter Name : ")
ide=int(input("Enter ID : "))
sub=input("Enter Subject : ")
dept=input("Enter Department : ")
p1=Teacher(ide,name,sub,dept)
p1.printval()