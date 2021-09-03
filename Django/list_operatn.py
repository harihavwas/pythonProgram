'''
lst=[2,4,6]
sum_lst=list(map(lambda num:sum(lst)-num,lst))
print(sum_lst)
'''

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

lst1=[10,11,20,21,22]
lst2=[13,14,20,21,30]
pos1=0
pos2=0
lst1[pos1]
while(pos1<len(lst1)):
    if (lst1[pos1]==lst2[pos2]):
        print(lst1[pos1])
        pos1+=1
        pos2+=1
    elif (lst1[pos1]>lst2[pos2]):
        pos2+=1
    else:
        pos1+=1