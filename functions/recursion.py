#Fctorail
"""def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
n=int(input("Enter number : "))
print("Factorial of ",n," = ",fact(n))"""



#Fibonascii
def fibo(n):
     if n<=1:
         return n
     else:
         return fibo(n-1)+fibo(n-2)
n=int(input("Enter limit : "))
for i in range(n):
    print(fibo(i))