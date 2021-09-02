class Bank:
    bal=0
    bank=input("Enter Bank : ")
    def crt(self):
        self.acc=int(input("Enter Account No : "))
        self.name=input("Enter Name : ")
        self.dob=input("Enter Date of Birth ; ")
        print("Account creted successfully")
    def dep(self):
        self.amt=int(input("Enter Deposite amount : "))
        self.bal=self.bal+self.amt
        print("Amount Credited successfully")
    def wdrw(self):
        self.wamt=int(input("Enter withdrawal amount : "))
        if (self.bal<=500):
            print("Minimum balance required")
        else:
            self.bal=self.bal-self.wamt
            print("Amount debited successfuly")
    def bale(self):
        print("Bank : ",Bank.bank)
        print("Account No : ",self.acc)
        print("Name : ",self.name)
        print("Current Balance : ",self.bal)
b1=Bank()
t=1
while (t):
    print("1. Create Account\n2. Deposite\n3. Withdraw\n4. Balance Enquiry")
    ch=int(input("Enter your choice : "))
    if ch==1:
        b1.crt()
    elif ch==2:
        b1.dep()
    elif ch==3:
        b1.wdrw()
    elif ch==4:
        b1.bale()
    else:
        print("Wrong choice")
    print("1. Go to menu\n0. Exit")
    t=int(input())