a=[1,2,3]
i=int(input("Enter Index : "))
try:
    print(a[i])
except:
    print("Index not excist")
finally:
    print("Indexing done successfully")