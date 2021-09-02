a=int(input("Enter age : "))
if a<18:
    raise Exception("Age provided is above 18")
else:
    print("You are eligible for vaccination")