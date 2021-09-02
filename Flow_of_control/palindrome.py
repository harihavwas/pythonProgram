# n=int(input("Enter any number"))
# rev=n
# d=0
# while (n>0):
#     s=int(n%10)
#     d=(d*10+s)
#     n=int(n/10)
# print(d)
# if (d==rev):
#     print("Palindrome")
# else:
#     print("Not palindrome")

a=input("Enetr value")
b=a[::-1]
if (a==b):
    print("Palindrome")
else:
    print("Not palindrome")