def srt(lst,l):
    for i in range(l):
        for j in range(i + 1, l):
            if (lst[i] > lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    print("Sorted List : ", lst)
    return lst

def bsearch(lst,l,s):
    slst=srt(lst,l)
    left=0
    right=l-1
    while (left<=right):
        mid=int(left+(right-1)/2)
        if slst[mid]==s:
            return 1
        elif slst[mid]<s:
            left=mid+1
        else:
            right=mid-1
    return -1

l = int(input("Enter limit : "))
lst = []
print('Enter list elements')
for i in range(l):
    lst.append(int(input()))
s = int(input("Enter element : "))
print("List : ", lst)
res=bsearch(lst, l,s)
if res==-1:
    print("Element Not Found")
else:
    print("Found")
