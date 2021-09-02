lst=[2,4,6]
sum_lst=list(map(lambda num:sum(lst)-num,lst))
print(sum_lst)

'''
lst3=[3,5,7]




lst2=[2,3,4,5]
sumf=int(input("Enter sum value : "))
# for i in range(len(lst2)):
#     for j in range(i+1,len(lst2)):
#         if ((lst2[i]+lst2[j])==sum):print(lst2[i],lst2[j])


pairs=[]
low=0
upp=len(lst2)-1
while(low<upp):
    sum=lst2[low]+lst2[upp]
    if sum==sumf:
        print(lst2[low],lst2[upp])
        #pairs.append(lst2[low],lst2[upp])
        low+=1
    elif(sum>sumf):
        upp-=1
    elif(sum<sumf):
        low+=1
'''