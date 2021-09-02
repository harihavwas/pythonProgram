# a=5
# if a>8:
#     print("Hello")
# else:
#     print("In else")
#
#
#
# # Positive or negative
#
# n=int(input("Enter any number"))
# if n>0:
#     print("Positive")
# else:
#     print("Negative")




# BANK ACCOUNT
fixed=1000
n=int(input("Enter withdraw amount : "))
if (n<=fixed):
    fixed-=n
    print("Balance amount : ",fixed)
else:
    print("Insufficient balance")