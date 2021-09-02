a=int(input("Enter a number : "))
b=int(input("Enter another number : "))
if b>a:
    raise Exception("No. 2 is greater")
else:
    print(a/b)