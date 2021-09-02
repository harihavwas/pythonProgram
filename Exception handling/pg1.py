a=[1,2,3]
p=int(input("Enter Index : "))
try:
    print(a[p])
except Exception as e:
    print(e.args)