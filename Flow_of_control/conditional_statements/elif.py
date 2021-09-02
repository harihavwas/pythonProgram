# POSITIVE OR NEGATIVE
# a=int(input("Enter any number : "))
# if (a>0):
#     print("Positive")
# elif (a<0):
#     print("Negative")
# else:
#     print("Zero")




# GREATER NUMBER
# a=int(input("Enter 1st number"))
# b=int(input("Enter 2d number"))
# if (a>b):
#     print(a," is greater")
# elif (a<b):
#     print(b," is greater")
# else:
#     print("Equal numbers")



# 3 numbers greater
a=int(input("Enter 1st number  : "))
b=int(input("Enter 2nd number  : "))
c=int(input("Enter 3rd number  : "))
if (a==b==c):
    print("All numberas are rqual")
else:
    if (a>b) & (a>c):
        print(a," is greater")
    elif (b>a) & (b>c):
        print(b," is greater")
    else:
        print(c," is greater")

