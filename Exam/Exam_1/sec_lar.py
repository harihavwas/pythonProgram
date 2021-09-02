lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print("Second Largest Element : ",lst[-2])