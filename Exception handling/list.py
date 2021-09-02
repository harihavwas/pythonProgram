lst=[1,2,3]
print("List : ",lst)
i=int(input("Enter index to print : "))
try:
    print(lst[i])
except:
    print("Exception Occured")