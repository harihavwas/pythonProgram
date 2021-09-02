"""
a=int(input("Enter a number : "))
b=int(input("Enter another number : "))
try:
    re=a/b
    print("Result : ",re)
except:
    print("Exception Occured")
"""


a=int(input("Enter a number : "))
b=int(input("Enter another number : "))
try:
    re=a/b
    print("Result : ",re)
except Exception as d:
    print(d.args)